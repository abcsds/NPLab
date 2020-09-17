import pyxdf
import matplotlib.pyplot as plt
import numpy as np

data, header = pyxdf.load_xdf('raw/BPresp.xdf')
markers = {}
for stream in data:
    y = stream['time_series']

    if isinstance(y, list):
        # list of strings, draw one vertical line for each marker
        for timestamp, marker in zip(stream['time_stamps'], y):
            plt.axvline(x=timestamp, c="red")
            print(f'Marker "{marker[0]}" @ {timestamp:.2f}s')
            markers[marker[0]] = timestamp
    elif isinstance(y, np.ndarray):
        # numeric data, draw as lines
        plt.plot(stream['time_stamps'], y)
        hr, resp, gsr = np.split(y, [1,2], axis=1)
    else:
        raise RuntimeError('Unknown stream format')
