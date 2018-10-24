import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv(r'BreadBasket_DMS.csv')
print(df.head())
print(df.info())
print(df.describe())

group_dt=df.groupby('Date')
#print(group_dt.agg(np.size))

group_by_dt=group_dt.agg(np.size)

print(group_by_dt.head())

print(group_by_dt.loc[group_by_dt['Transaction'].max()])