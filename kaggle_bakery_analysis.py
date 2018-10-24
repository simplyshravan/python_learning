import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv(r'BreadBasket_DMS.csv')
#print(df.head())
#print(df.info())
#print(df.describe())
month_col=df['Date'].values
month_col= [ my_str.split("-")[1] for my_str in month_col ]
df['Month']=month_col
month_col=df['Date'].values
month_col= [ my_str.split("-")[0] for my_str in month_col ]
#print(month_col)
df['Year']=month_col
print(df.info())
print(df.head())


#df1=df[['Transaction','Year']]


group_dt=df.groupby(['Year','Month']).agg(np.size)
#print(group_dt.agg(np.size))
print(group_dt.head())
#group_month=df.groupby(['Date','Month'])
#group_dt.agg(np.size)
#print(group_by_dt.info())
#print(group_by_dt.head())
print(group_dt['Transaction'].max())

print(group_dt[group_dt['Transaction']==group_dt['Transaction'].max()])

#sns.pairplot(group_dt)

#sns.distplot(group_dt['Transaction'])
#sns.countplot(x=df['Year'],hue=df['Month'],data=df)

sns.pairplot(df)
#group_dt=df.groupby(['Date','Month'])


#sns.countplot(x=df['Month'],data=df)
