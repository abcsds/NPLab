import pyxdf
import matplotlib.pyplot as plt
import numpy as np

data, header = pyxdf.load_xdf('analysis/raw/BPresp.xdf')
markers = {}
plt.figure(figsize=(20, 7))
for stream in data:
    y = stream['time_series']
    if isinstance(y, list):
        # list of strings, draw one vertical line for each marker
        for timestamp, marker in zip(stream["time_stamps"], y):
            plt.axvline(x=timestamp, c="red")
            print(f'Marker "{marker[0]}" @ {timestamp:.2f}s')
            markers[marker[0]] = timestamp
    elif isinstance(y, np.ndarray):
        # numeric data, draw as lines
        fs = int(stream["info"]["nominal_srate"][0])
        plt.plot(stream["time_stamps"], y)
        ecg, resp, gsr = np.split(y, [1,2], axis=1)
        t = stream["time_stamps"]
    else:
        raise RuntimeError('Unknown stream format')


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

def notch_filter(data, fs, f0=50, Q=2):
    b, a = signal.iirnotch(f0, Q, fs)
    y = signal.lfilter(b, a, data)
    return y

filtered_sig = notch_filter(butter_bandpass(ecg, 0.01, .1, fs), fs)
filtered_sig = ecg

samples = 6000
plt.figure(figsize=(16, 7))
plt.title("ECG signal")
plt.plot(t[0:samples], filtered_sig[0:samples], color="#51A6D8", linewidth=1)
plt.xlabel("Time (s)", fontsize=16)
plt.ylabel("Amplitude (arbitrary unit)")
plt.show()


import heartpy as hp

hrdata = ecg.flatten()

filtered = hp.filter_signal(hrdata,
                            cutoff=[0.75, 3.5],
                            sample_rate=fs,
                            order=3,
                            filtertype='bandpass')

filtered = hp.filter_signal(filtered,
                            cutoff=1,
                            sample_rate=fs,
                            filtertype='notch')

working_data, measures = hp.process(hrdata, fs)
plt.figure(figsize=(150, 7))
plt.title("ECG signal")
hp.plotter(working_data, measures)
