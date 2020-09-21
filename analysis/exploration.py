import pyxdf
import matplotlib.pyplot as plt
import numpy as np


data, header = pyxdf.load_xdf('analysis/raw/000.xdf')

plt.figure(figsize=(16, 7))
markers = {}
# with data[0] as stream: # RDA external electrodes
stream = data[0]
y = stream['time_series']
# numeric data, draw as lines
fs = int(stream["info"]["nominal_srate"][0])
plt.plot(stream["time_stamps"], y)
ecg, resp, gsr = np.split(y, [1, 2], axis=1)
t = stream["time_stamps"]
# with data[2] as stream:
stream = data[2]
for marker, ts in zip(stream["time_series"], stream["time_stamps"]):
    plt.axvline(x=ts, c="red")
    markers[marker[0]] = ts
plt.show()

# signal processing
from scipy import signal
from scipy.ndimage import label
from scipy.stats import zscore
from scipy.interpolate import interp1d
from scipy.integrate import trapz


def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    y = signal.lfilter(b, a, data)
    return y


def notch_filter(data, fs, f0=50, Q=30):
    b, a = signal.iirnotch(f0, Q, fs)
    y = signal.lfilter(b, a, data)
    return y


def detrend_filter(data):
    return data - data.mean()


non_filtered = detrend_filter(-ecg)
# non_filtered = -ecg
filtered_sig = bandpass_filter(non_filtered, 0.01, 45, fs)
filtered_sig = notch_filter(filtered_sig, fs)

samples = 6000
plt.figure(figsize=(16, 7))
plt.title("ECG signal")
plt.plot(t[0:samples], filtered_sig[0:samples], color="#51d79b", linewidth=1)
plt.plot(t[0:samples], non_filtered[0:samples], color="#51A6D8", linewidth=1)
plt.xlabel("Time (s)", fontsize=16)
plt.ylabel("Amplitude (uV)")
plt.show()

from biosppy.signals import ecg

# load raw ECG signal
sig = non_filtered.flatten()

# process it and plot
out = ecg.ecg(signal=sig, sampling_rate=fs, show=True)

plt.figure(figsize=(200, 7))
plt.plot(out["ts"], out["filtered"],
         color="#51A6D8",
         linewidth=1)
plt.scatter(out["ts"][out["rpeaks"]],
            out["filtered"][out["rpeaks"]],
            color="#df4040",
            linewidth=1)
plt.xlim(0, 290)

plt.figure(figsize=(16, 7))
for y in out["templates"]:
    plt.plot(out["templates_ts"], y, color="#51A6D8", linewidth=1, alpha=0.2)


plt.figure(figsize=(16, 7))
plt.plot(out["heart_rate_ts"], out["heart_rate"],
         color="#51A6D8",
         linewidth=1)

# R-R intervals
rr_intervals = np.diff(out["ts"][out["rpeaks"]], prepend=[np.nan])
rr_intervals *= 1000  # Convert from s to ms

stream = data[2]
plt.figure(figsize=(16, 7))
plt.plot(out["ts"][out["rpeaks"]] + stream["time_stamps"].min(),
         rr_intervals)
for marker, ts in zip(stream["time_series"], stream["time_stamps"]):
    plt.axvline(x=ts, c="red")
plt.xlabel("Time (s)")
plt.ylabel("RR-interval (ms)")

# Rolling window for SDNN
def rolling_std(vec, window_size):
    shape = vec.shape[:-1] + (vec.shape[-1] - window_size + 1, window_size)
    strides = vec.strides + (vec.strides[-1],)
    windows = np.lib.stride_tricks.as_strided(vec,
                                              shape=shape,
                                              strides=strides)
    rstd = np.hstack((np.zeros(window_size // 2) + np.nan,
                      np.std(windows, 1),
                      np.zeros((window_size // 2) - 1) + np.nan))
    return rstd


n = 8 # Must be even number for now
hrv = rolling_std(rr_intervals, n)
plt.figure(figsize=(16, 7))
plt.plot(out["ts"][out["rpeaks"]] + stream["time_stamps"].min(),
         hrv,
         color="#51A6D8")
for marker, ts in zip(stream["time_series"], stream["time_stamps"]):
    plt.axvline(x=ts, c="red")
plt.xlabel("Time (s)")
plt.ylabel("SDNN (ms)")

# Segmentation
# Relevant segments are between markers (2,3), and (4,5)
# Segment variables in seconds
out["heart_rate"].shape
hrv.shape
rr_intervals.shape
time = out["ts"][out["rpeaks"]] + stream["time_stamps"].min()
time.shape
baseline_time = np.where((markers[2] < time) & (time < markers[3]))
baseline_hr = out["heart_rate"][baseline_time]
baseline_hrv = hrv[baseline_time]
baseline_rr = rr_intervals[baseline_time]

condition_time = np.where((markers[4] < time) & (time < markers[5]))
condition_hr = out["heart_rate"][condition_time]
condition_hrv = out["heart_rate"][condition_time]
condition_rr = rr_intervals[condition_time]

# Segment variables in samples
resp.shape
gsr.shape
t.shape
baseline_t = np.where((markers[2] < t) & (t < markers[3]))
baseline_gsr = gsr[baseline_t]
baseline_resp = resp[baseline_t]

condition_t = np.where((markers[4] < t) & (t < markers[5]))
condition_gsr = gsr[condition_t]
condition_resp = resp[condition_t]

# TODO: breath amplitude, gsr mean.
# Build results table
import pandas as pd


res = {"Variable": ["HR (BPM)",
                    "HRV (SDNN)",
                    "Resp (arb)",
                    "GSR (arb)"],
       "Baseline": [baseline_hr.mean(),
                    baseline_rr.std(),
                    baseline_resp.std(),
                    baseline_gsr.mean()],
       "Condition": [condition_hr.mean(),
                     condition_rr.std(),
                     condition_resp.std(),
                     condition_gsr.mean()]}
results = pd.DataFrame(res)
results.to_csv("./analysis/results.csv", index=False, float_format="%.4f")
