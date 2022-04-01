#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv(r"https://raw.githubusercontent.com/edyoda/data-science-complete-tutorial/master/Data/Shopping_Revenue.csv")
df.head()


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


#checking missing value
df.isnull().sum()


# In[65]:


#Filling missing value
df['P6'].mean()
df['P6']=df['P6'].fillna(df['P6'].mean())


# In[66]:


df['P7'].mean()
df['P7']=df['P7'].fillna(df['P7'].mean())


# In[68]:


df.head()


# In[69]:


#Data Analysis
plt.figure(figsize=(35,6))
sns.countplot(x='City',data=df)
plt.show()


# In[70]:


plt.figure(figsize=(6,6))
sns.countplot(x='City Group',data=df)
plt.show()


# In[71]:


plt.figure(figsize=(6,6))
sns.countplot(x='Type',data=df)
plt.show()


# In[72]:


#Data Preprocessing(Converting object type data into int)
df['City'].value_counts()


# In[73]:


#label encoding
from sklearn.preprocessing import LabelEncoder
encoder= LabelEncoder()
df['City']=encoder.fit_transform(df['City'])
df['City Group']=encoder.fit_transform(df['City Group'])
df['Type']=encoder.fit_transform(df['Type'])
df.head()


# In[134]:



df.drop('City Group',axis = 1,inplace=True)
df.drop('Type',axis=1,inplace=True)


# In[135]:


df.info()


# In[136]:


#Splitting Features And Target
X=df.drop('revenue',axis=1)
y=df['revenue']


# In[137]:


print(X)


# In[138]:


print(y)


# In[139]:


#splitting data into training data testing data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)


# In[140]:


get_ipython().system('pip install xgboost')


# In[141]:


#model selection and model training
from xgboost import XGBRegressor
from sklearn import metrics


# In[142]:


regressor = XGBRegressor()
regressor.fit(X_train,y_train)


# In[143]:


#Training data
train_data_prediction=regressor.predict(X_train)


# In[144]:


#R square value
r2_train=metrics.r2_score(y_train,train_data_prediction)
print('R Squared Value=',r2_train)


# In[145]:


#testing data
test_data_prediction=regressor.predict(X_test)


# In[146]:


#R square value
r2_test=metrics.r2_score(y_test,test_data_prediction)
print('R Squared Value=',r2_test)


# In[116]:


X.shape,X_train.shape,X_test.shape


# In[117]:


#Linear Regression
from sklearn import metrics
from sklearn.linear_model import LinearRegression


# In[118]:


lin_reg_model=LinearRegression()
lin_reg_model.fit(X_train,y_train)


# In[119]:


#predicting on training data
lin_train_data_prediction=lin_reg_model.predict(X_train)


# In[120]:


#R Squared error
error_score= metrics.r2_score(y_train,lin_train_data_prediction)
print("R Squared Error:",error_score)


# In[121]:


#visualization
plt.scatter(y_train,lin_train_data_prediction)
plt.xlabel('Actual Revenue')
plt.ylabel('Predicted Revenue')
plt.show()


# In[122]:


#predicting on testing data
lin_test_data_prediction=lin_reg_model.predict(X_test)


# In[123]:


#R Squared error
error_score= metrics.r2_score(y_test,lin_test_data_prediction)
print("R Squared Error:",error_score)


# In[124]:


#visualization
plt.scatter(y_test,lin_test_data_prediction)
plt.xlabel('Actual Revenue')
plt.ylabel('Predicted Revenue')
plt.show()


# In[ ]:





# In[125]:


from sklearn.linear_model import Lasso


# In[126]:


lass_reg_model=Lasso()
lass_reg_model.fit(X_train,y_train)


# In[127]:


#predicting on training data
laso_train_data_prediction=lass_reg_model.predict(X_train)


# In[128]:


#R Squared error
error_score= metrics.r2_score(y_train,laso_train_data_prediction)
print("R Squared Error:",error_score)


# In[129]:


#visualization
plt.scatter(y_train,laso_train_data_prediction)
plt.xlabel('Actual Revenue')
plt.ylabel('Predicted Revenue')
plt.show()


# In[130]:


#predicting on testing data
laso_test_data_prediction=lass_reg_model.predict(X_test)


# In[131]:


#R Squared error
error_score= metrics.r2_score(y_test,laso_test_data_prediction)
print("R Squared Error:",error_score)


# In[132]:


#visualization
plt.scatter(y_test,lin_test_data_prediction)
plt.xlabel('Actual Revenue')
plt.ylabel('Predicted Revenue')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




