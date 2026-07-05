import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.signal import butter,filtfilt
df = pd.read_csv("data/mitbih_train.csv", header=None)
heartbeat = df.iloc[0, 0:187].values
#BUTTERWORTH FILTER
fs=360
lowcut=0.5
highcut=40
nyquist=fs/2
b,a=butter(
    4,
    [lowcut/nyquist,highcut/nyquist],
    btype="band"
)
filtered=filtfilt(b,a,heartbeat)

plt.figure(figsize=(12,5))
plt.plot(heartbeat,label="Original ECG")
plt.plot(filtered,label="Filtered ECG")
plt.legend()
plt.title("Original vs Filtered ECG")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid()
print("Minimum:", heartbeat.min())
print("Maximum:", heartbeat.max())
print("Mean:", heartbeat.mean())

print("Filtered Minimum:", filtered.min())
print("Filtered Maximum:", filtered.max())
print("Filtered Mean:", filtered.mean())
plt.show()
