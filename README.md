# Neurophysiology lab
Within this repo you can find the files necessary for the Neurophysiology laboratory at the TU Graz that focuses on three signal measurements: Electrocardiogram (ECG), Galvanic skin response (GSR), and Respiration.

The experiment is constructed of two parts:
 - The cognitive experiment program, within the `main.py` file was generated with [Psychopy](https://www.psychopy.org/), and uses `pylsl` to connect to the Lab streamer program. To run the experiment type `python main.py` from a command line. The result of this meassuring should be stored as an XDF file, through the [lab streamer software](https://github.com/sccn/labstreaminglayer).
 - The analysis is to be done on the XDF file, and a small script and [Jupyter notebook](https://jupyter.org/) are provided to review and adapt the analysis code to your own needs.

An example file is provided, you can run the analysis on it with the following command:
```
python analysis/main.py analysis/raw/000.xdf
```


## Setup
To setup the environment install [Python 3.8](https://www.python.org/) or above, and install the required libraries with the following command:

```
pip install -r requirements.txt
```

This should install the requirements to run the cognitive experiment, and the libraries for the analysis script.

As a stimulus, the video called `Dragon.mp4` was used. This is a [clip from the movie "Dragon: The Bruce Lee Story"](https://www.youtube.com/watch?v=jZZMDc5PwzE). This video is not included for copy right reasons, but you can include it yourself by placing it under the folder for experimental data `exp_data`, or select a different video as a stimulus and add the path to the file `main.py` that contains the Psychopy experiment.


## Modifying the code
This laboratory will be a simple demonstration this year. For this reason, we encourage you to explore the experiment, data, and code provided, and modify it to accommodate your needs.
