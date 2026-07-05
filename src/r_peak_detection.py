import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
df=pd.read_csv("data/mitbih_train.csv",header=None)
heartbeat = df.iloc[0,0:187].values
peaks,properties =find_peaks(
    heartbeat,
    height=0.5,
    distance=50
)
plt.figure(figsize=(12,5))

plt.plot(heartbeat, label="ECG")
plt.plot(
    peaks,
    heartbeat[peaks],
    "ro",
    label="R Peaks"
)

plt.title("Detected R Peaks")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.show()
print("Detected Peaks:",peaks)
print("Number of peaks:",len(peaks))