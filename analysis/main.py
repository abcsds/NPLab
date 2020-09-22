#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Alberto Barradas"
__version__ = "0.1.0"
__license__ = "MIT"
import pyxdf  # Open xdf files
import argparse  # Read arguments from command line
import numpy as np  # Numeric library for python
import pandas as pd  # Tabular DataFrames
from os import path  # Filenames and path handling
from scipy import signal  # Digital Signal Processing
from biosppy.signals import ecg  # ECG algorithms


def bandpass_filter(data, lowcut, highcut, fs, order=4):
    """Butterworth bandpass filter"""
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    y = signal.lfilter(b, a, data)
    return y


def rolling_std(vec, window_size):
    """Rolling window for SDNN"""
    shape = vec.shape[:-1] + (vec.shape[-1] - window_size + 1, window_size)
    strides = vec.strides + (vec.strides[-1],)
    windows = np.lib.stride_tricks.as_strided(vec,
                                              shape=shape,
                                              strides=strides)
    rstd = np.hstack((np.zeros(window_size // 2) + np.nan,
                      np.std(windows, 1),
                      np.zeros((window_size // 2) - 1) + np.nan))
    return rstd


def breath_frequency(sig, fs, filter=False):
    """
    Returns the peak frequency in bpm of a spectrum within the bounds
    of respiration frequencies
    """
    if filter:
        sig = bandpass_filter(sig, 0.05, .4, fs)  # 3-24 breaths per minute
    ps = np.abs(np.fft.fft(sig))**2
    freqs = np.fft.fftfreq(sig.size, 1 / fs)
    idx = np.argsort(freqs)
    b_idx = np.where((0.1 < freqs[idx]) & (freqs[idx] < 0.4))
    b_freqs = freqs[idx][b_idx]
    b_ps = ps[idx][b_idx]
    imax = np.argmax(b_ps)
    return b_freqs[imax] * 60  # convert to BPM


def main(args):
    file_path = args.file_path
    file_name = path.basename(file_path)[:-4]
    data, header = pyxdf.load_xdf(file_path)

    # Read the biosignals from the first stream
    stream = data[0]
    y = stream['time_series']
    fs = int(stream["info"]["nominal_srate"][0])  # Store sample frequency (fs)
    ecg_sig, resp, gsr = np.split(y, [1, 2], axis=1)  # Store three biosignals
    t = stream["time_stamps"]  # Extract time array

    # Read the markers from the third stream
    stream = data[2]
    markers = {}  # A variable to store the markers
    for marker, ts in zip(stream["time_series"], stream["time_stamps"]):
        markers[marker[0]] = ts

    # load raw ECG signal
    out = ecg.ecg(signal=ecg_sig.flatten(), sampling_rate=fs, show=False)

    # Extract rr_intervals
    rr_intervals = np.diff(out["ts"][out["rpeaks"]], prepend=[np.nan])
    rr_intervals *= 1000  # Convert from s to ms

    # Segment variables in seconds
    time = out["ts"][out["rpeaks"]] + stream["time_stamps"].min()
    baseline_time = np.where((markers[2] < time) & (time < markers[3]))
    baseline_hr = out["heart_rate"][baseline_time]
    baseline_rr = rr_intervals[baseline_time]

    condition_time = np.where((markers[4] < time) & (time < markers[5]))
    condition_hr = out["heart_rate"][condition_time]
    condition_rr = rr_intervals[condition_time]

    # Segment variables in samples
    baseline_t = np.where((markers[2] < t) & (t < markers[3]))
    baseline_gsr = gsr[baseline_t]
    baseline_resp = resp[baseline_t]

    condition_t = np.where((markers[4] < t) & (t < markers[5]))
    condition_gsr = gsr[condition_t]
    condition_resp = resp[condition_t]

    # Build results table
    res = {"Variable": ["HR (BPM)",
                        "HRV (SDNN)",
                        "Resp (arb)",
                        "GSR (arb)"],
           "Baseline": [baseline_hr.mean(),
                        baseline_rr.std(),
                        breath_frequency(baseline_resp, fs),
                        baseline_gsr.mean()],
           "Condition": [condition_hr.mean(),
                         condition_rr.std(),
                         breath_frequency(condition_resp, fs),
                         condition_gsr.mean()]}
    results = pd.DataFrame(res)
    save_path = path.join([".", "analysis", "results", f"{file_name}_res.csv"])
    results.to_csv(save_path, index=False, float_format="%.4f")
    print("DONE")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="XDF file to be processed")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))
    args = parser.parse_args()
    main(args)
