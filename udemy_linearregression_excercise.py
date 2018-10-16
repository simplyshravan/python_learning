import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

ec=pd.read_csv('Ecommerce Customers')

print(ec.head())

print(ec.info())

print(ec.columns)

print(ec.describe())

sns.set_style("whitegrid", {'axes.grid' : True})

# Joitplot different syntax 
print(sns.jointplot(x=ec['Time on Website'],y= ec['Yearly Amount Spent'], color="k"))

print(sns.jointplot(x=ec['Time on Website'],y= ec['Yearly Amount Spent'], color="k").plot_joint(sns.kdeplot, zorder=0, n_levels=6))


print(sns.jointplot(x='Time on App',y= 'Yearly Amount Spent',data=ec, color="k"))

print(sns.jointplot('Time on App','Yearly Amount Spent',data=ec, color="k").plot_joint(sns.kdeplot, zorder=0, n_levels=6))

#grid on and off in seaborn
sns.set_style("whitegrid", {'axes.grid' : False})
print(sns.jointplot('Time on App','Length of Membership',data=ec, color="k",kind='hex'))

sns.pairplot(ec)

sns.set_style("whitegrid", {'axes.grid' : True})
sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data=ec)

#Predicting model

X=ec[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
y=ec['Yearly Amount Spent']

X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=.3,random_state=101)

lm = LinearRegression()
lm.fit(X_train,y_train)

print(lm.coef_)

predictions=lm.predict(X_test)

plt.grid(b=True)

plt.scatter(y_test,predictions)

print(metrics.mean_squared_error(y_test,predictions))
print(metrics.mean_absolute_error(y_test,predictions))
print(np.sqrt(metrics.mean_squared_error(y_test,predictions)))

sns.distplot(y_test-predictions,bins=30,hist=True)

plt.hist(y_test-predictions,bins=30)

print(lm.intercept_)

print(lm.coef_)
