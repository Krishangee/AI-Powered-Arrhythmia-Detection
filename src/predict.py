import joblib
import pandas as pd
model = joblib.load("arrhythmia_model.pkl")

print("Model loaded successfully!")
df = pd.read_csv("data/mitbih_test.csv", header=None)

sample = df.iloc[0, 0:187]

print(sample.head())
sample = sample.values.reshape(1, -1)

print(sample.shape)
prediction = model.predict(sample)
print("Predicted Class:", prediction[0])
class_names = {
    0: "NORMAL",
    1: "SVEB",
    2: "VEB",
    3: "FUSION",
    4: "UNKNOWN"
}
print("Predicted Heartbeat:", class_names[int(prediction[0])])