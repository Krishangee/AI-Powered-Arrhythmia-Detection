import pandas as pd
#Load ECG dataset
df=pd.read_csv("data/mitbih_train.csv",header=None)
#Select one heartbeat
heartbeat=df.iloc[0,0:187]
print("Minimum value:",heartbeat.min())
print("Maximum value:",heartbeat.max())