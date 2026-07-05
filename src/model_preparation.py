import pandas as pd
df=pd.read_csv("data/mitbih_train.csv",header=None)
x=df.iloc[:,0:187]
y=df.iloc[:,187]
print("X Shape:", x.shape)
print("Y Shape:", y.shape)

print("\nFirst ECG:")
print(x.head())

print("\nLabels:")
print(y.head())