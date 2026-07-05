import pandas as pd
df= pd.read_csv("data/mitbih_test.csv",header=None)
print("Shape:",df.shape)
print("\nData Types:")
print(df.dtypes.value_counts())
print("\nMissing Values: ")
print(df.isnull().sum())
print("\nClass Distribution: ")
print(df[187].value_counts())