import pandas as pd

# Load MIT-BIH training dataset
df = pd.read_csv("data/mitbih_train.csv", header=None)

print("Dataset Shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nClass Distribution:")
print(df[187].value_counts())

import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))

for i in range(5):
    heartbeat = df.iloc[i, 0:187]
    plt.plot(heartbeat, label=f"Beat {i}")

plt.title("First 5 ECG Heartbeats")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
print(df.iloc[:10, 187])
