#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df=pd.read_table(r"https://raw.githubusercontent.com/edyoda/data-science-complete-tutorial/master/Data/epilepsy.data",sep=",")
df.head()


# In[8]:


df.describe()


# In[9]:


df.columns


# In[10]:


df.shape


# In[11]:


df.info()


# In[12]:


df.isnull().sum()


# In[13]:


#Filling missing value with mode
df['MDVP:PPQ'].mode()[0]


# In[14]:


df['Jitter:DDP'].mode()[0]


# In[15]:


df['MDVP:PPQ']=df['MDVP:PPQ'].fillna(df['MDVP:PPQ'].mode()[0])


# In[16]:


df['Jitter:DDP']=df['Jitter:DDP'].fillna(df['Jitter:DDP'].mode()[0])


# In[17]:


df.isnull().sum()


# In[19]:


df.info()


# In[20]:


df['status'].unique()


# In[21]:


df['status'].value_counts()


# In[24]:


#grouping data based on target variables.
df.groupby('status').mean()


# In[45]:


#seperating features and target 
X=df.drop(columns=['name','status'],axis=1)
y=df['status']
print(X)


# In[46]:


print(y)


# In[47]:


#Train Test Split
from sklearn.model_selection import train_test_split


# In[77]:


X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=2)


# In[78]:


#data standarization
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


# In[79]:


print(X_train.shape,y_train.shape)


# In[80]:


#model traing (SVM Algorithm)
from sklearn import svm
from sklearn.metrics import accuracy_score


# In[81]:


model= svm.SVC(kernel='linear')
model.fit(X_train,y_train)


# In[89]:


#accuracy
X_train_prediction=model.predict(X_train)
training_data_accuracy=accuracy_score(y_train,X_train_prediction)
print('Accuracy score of training data :',training_data_accuracy)


# In[90]:


X_test_prediction=model.predict(X_test)
testing_data_accuracy=accuracy_score(y_test,X_test_prediction)
print('Accuracy score of testing data :',testing_data_accuracy)


# In[91]:


#Using KNN Algo.
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train,Y_train)


# In[92]:


y_pred=classifier.predict(X_test)


# In[93]:


from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))


# In[94]:


#Since the accuracy with the help of KNN Algorithm is low .we will move with SVM Algorithm.


# In[95]:


#Predictive System
input_data = (116.67600,137.87100,111.36600,0.00997,0.00009,0.00502,0.00698,0.01505,0.05492,0.51700,0.02924,0.04005,0.03772,0.08771,0.01353,20.64400,0.434969,0.819235,-4.117501,0.334147,2.405554,0.368975)
#changing data types
new_input_data=np.asarray(input_data)
reshaped_input_data=new_input_data.reshape(1,-1)


# In[97]:


std_data=sc.transform(reshaped_input_data)
prediction=model.predict(std_data)
print(prediction)
if(prediction[0]==0):
    print("Healthy People")
else:
    print("People Having The Disease")


# In[ ]:




