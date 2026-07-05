import pandas as pd
import matplotlib.pyplot as plt
#Load training dataset
df = pd.read_csv("data/mitbih_train.csv",header=None)
#Counter heartbeats in each class
class_counts=df[187].value_counts()
print(class_counts)

plt.figure(figsize=(8,5))

class_counts.plot(kind="bar")
plt.xticks(
    ticks=[0,1,2,3,4],
    labels=[
        "Normal",
        "Supraventricular",
        "Ventricular",
        "Fusion",
        "Unknown"
    ],
    rotation=20
)

plt.title("Heartbeat Class Distribution")
plt.xlabel("Heartbeat Type")
plt.ylabel("Number of Samples")
plt.grid(axis="y")

plt.show()