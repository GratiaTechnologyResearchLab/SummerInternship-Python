
# coding: utf-8

# In[65]:


#IMPORTING THE LIBRARIES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


# In[66]:


#IMPORT THE TRAINING DATASET

trainset=pd.read_csv('train.csv')

#CHECK FOR THE OUTLIERS AND REMOVE IT FROM THE DATASET

trainset=trainset[(np.abs(stats.zscore(trainset))<3).all(axis=1)]

#SEPARATE THE DEPENDENT AND THE INDEPENDENT VARIABLE(COLOUMN)

xtrain=trainset.iloc[:,:-1].values
ytrain=trainset.iloc[:,1].values



# In[67]:


#IMPORT THE TEST DATASET

testset=pd.read_csv('test.csv')

#CHECK FOR THE OUTLIERS AND REMOVE IT FROM THE DATASET

testset=testset[(np.abs(stats.zscore(testset))<3).all(axis=1)]

#SEPARATE THE DEPENDENT AND THE INDEPENDENT VARIABLE(COLOUMN)

xtest=testset.iloc[:,:-1].values
ytest=testset.iloc[:,1].values



# In[68]:


#FEATURE SCALING

from sklearn.preprocessing import StandardScaler

sc_X=StandardScaler()
xtrain=sc_X.fit_transform(xtrain)
xtest=sc_X.fit_transform(xtest)


# In[69]:


#FIT THE LINEAR REGRESSOR TO THE TRAINING SET

from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
regressor.fit(xtrain,ytrain)


# In[70]:


#PLOT AND COMPARE YOUR TRAINING SET WITH THE TEST SET

plt.scatter(xtest,ytest, color='red')
plt.plot(xtest,regressor.predict(xtest), color='blue')
plt.xlabel('X-Values')
plt.ylabel('Y-Values')
plt.title('***Linear Regression Model-I***')
plt.show()


# In[ ]:




