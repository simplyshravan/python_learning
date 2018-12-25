import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

df=pd.read_csv(r'E:\GitHub\python_learning\KNN_Project_Data')

print(df.head())
print(df.columns)

#EDA
sns.pairplot(df,hue='TARGET CLASS')

sns.pairplot(df,hue='TARGET CLASS',palette='coolwarm')

#standardize the variables
scaler=StandardScaler()
scaler.fit(df.drop('TARGET CLASS',axis=1))
scaled_feat=scaler.transform(df.drop('TARGET CLASS',axis=1))
df_feat=pd.DataFrame(scaled_feat,columns=df.columns[:-1])

#preparing data for model
X=df_feat
Y=df['TARGET CLASS']
X_train, X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.33,random_state=101)

#training model
knc=KNeighborsClassifier(n_neighbors=1)
knc.fit(X_train,Y_train)
pred=knc.predict(X_test)

#measuring model
print(confusion_matrix(Y_test,pred))
print(classification_report(Y_test,pred))

#lets see for other values of n_neighbors
error_rate=[]

for i in range(1,40):
    knc=KNeighborsClassifier(n_neighbors=i)
    knc.fit(X_train,Y_train)
    pred=knc.predict(X_test)
    error_rate.append(np.mean(pred!=Y_test))
    
#plotting error rate for diffrent valeus of n_neighbors
plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue',linestyle='dashed',marker='o',markerfacecolor='red',markersize=10)
plt.title('Error Rate vs K value')
plt.xlabel('K value')
plt.ylabel('Error Rate')

#choosing n_neighbors=30
knc=KNeighborsClassifier(n_neighbors=30)
knc.fit(X_train,Y_train)
pred=knc.predict(X_test)
print(confusion_matrix(Y_test,pred))
print(classification_report(Y_test,pred))












