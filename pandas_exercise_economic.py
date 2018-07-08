# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 13:06:19 2018

@author: DELL
"""
import numpy as np
import pandas as pd
df=pd.read_csv('Ecommerce Purchases')
#print(df.loc[0])
print(df.head())
print(df.info)
print(df.shape)
print(df['Purchase Price'].mean())
print(df['Purchase Price'].max())
print(df['Purchase Price'].min())

#How many people have English 'en' as their Language of choice on the website?
print(df.groupby('Language').count().loc['en'])
print(df[df['Language']=='en'].count())
print(df.groupby('Job').count().loc['Lawyer'])
print(df[df['Job']=='Lawyer'].count())
print(pd.value_counts(df['AM or PM']))
print(df['AM or PM'].value_counts())
print(df['Job'].value_counts().head(5))
#top 5 jobs
print(pd.value_counts(df['Job'].sort_values(ascending=False)).head())
#purchase from lot  90 WT
print(df[df['Lot']=='90 WT'][['Purchase Price','Address']])#,'Address'])
#4926535242672853 
print(df[df['Credit Card']==4926535242672853]['Email'])
print(df[(df['CC Provider']=='American Express') & (df['Purchase Price']>95)].count())
#print(df['CC Exp Date'].str[3:])
#print(df['CC Exp Date'].dt.year)
print(df[df['CC Exp Date'].str[3:] == '25'].count())
print(sum(df['CC Exp Date'].apply(lambda x: x[3:]) == '25'))
#print(pd.value_counts(df['CC Exp Date'].str[3:]=='25'))
#count top 5 domains
#print(df['Email'].str.split("@").str[-1])
#print(df['Email'].str.split("@").str[-1])
df1=df['Email'].str.split("@").str[-1]
df2=pd.DataFrame(df1)
print(pd.value_counts(df2['Email'].sort_values(ascending=False)).head())
print(df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))

#df1=pd.Series(data=df2,['a','b'])
#print(df1)
#print(df1.groupby('Email').count())

#print(df[df['Email'].str.split("@").str[-1]].count())#.sort_values(ascending=False)).head())
#print(pd.value_counts(df['Job'].head()))
#print(df.describe)