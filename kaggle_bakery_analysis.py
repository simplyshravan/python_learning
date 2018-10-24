import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime

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
month_col=df['Date'].values
month_col= [ my_str.split("-")[2] for my_str in month_col ]
#print(month_col)
df['Day']=month_col

#print(df.info())
#print(df.head())

print(datetime.date(2016, 10, 30).weekday())
month_col=df['Date'].values
month_col= [ datetime.date(int(my_str.split("-")[0]),int( my_str.split("-")[1]), int(my_str.split("-")[-1])).weekday() for my_str in month_col ]
#print(month_col)
df['Weekday']=month_col
#print(df.head())
#print(df.columns)
df1=df[['Transaction', 'Month', 'Year', 'Day','Weekday']]
print(df1.head())

#df1=df[['Transaction','Year']]

df1.drop_duplicates(inplace=True)
group_yr=df1.groupby(['Year']).agg(np.size)
print(group_yr.head())

group_weekday=df1.groupby(['Weekday']).agg(np.size)
print(group_weekday)

group_mth=df1.groupby(['Month']).agg(np.size)
print(group_mth)
#sns.countplot(x=group_weekday['Transaction'],y=group_weekday['Weekday'],data=group_weekday)

#sns.countplot(x=group_yr['Year'],data=group_yr)
#sns.barplot(x='Month', y='Transaction', hue='Year', data=df1)

sns.barplot(x='Weekday', y='Transaction', hue='Year', data=df1)
#sns.barplot(x=df1['Month'],data=df1)
#sns.scatterplot(df1)
#print(group_dt.agg(np.size))
#print(group_dt.head())
#group_month=df.groupby(['Date','Month'])
#group_dt.agg(np.size)
#print(group_by_dt.info())
#print(group_by_dt.head())
#print(group_dt['Transaction#'].max())

#print(group_dt[group_dt['Transaction']==group_dt['Transaction'].max()])

#sns.pairplot(group_dt)
#df2016=df[df['Year']=='2017']
#print(df2016.head())
#print(df2016['Month'].unique())

#sns.distplot(group_dt['Transaction'])
#during Nov or we can say festive season the sale is higher
#sns.countplot(x=df['Month'],y=df['Year'],hue=df['Year'],data=df)
#sns.countplot(x=df['Month'],y=df['Year'],data=df)

#f, ax = plt.subplots(1, 1)
#sns.pointplot(ax=ax,x=df['Year'],y=df['Transaction'],data=df,color='blue')


#sns.catplot(x=df['Year'],hue=df['Month'],col='Weekday',data=df,kind="count", height=4, aspect=.7);

#sns.pairplot(df)
#group_dt=df.groupby(['Date','Month'])


#sns.countplot(x=df['Month'],data=df)
