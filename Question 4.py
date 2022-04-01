#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('capture', '', "!pip install -U gspread\n!pip install -U requests\nfrom io import BytesIO\nimport warnings\nwarnings.filterwarnings('ignore')\nimport requests\nimport pandas as pd\nimport gspread")


# In[2]:


url="https://docs.google.com/spreadsheets/d/1Y_g6LQI2GLqpKf-fj-rH7D9gfnP2MJzpFA6t0AsBMi8/edit#gid=0"


# In[11]:


credentials={
  "type": "service_account",
  "project_id": "edyoda-345516",
  "private_key_id": "4210270da0bdd952c3b6ebaba910d003918861fb",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCFw52yeVPtMc/n\nQyZHyTEMbrcuiIky5ZyjsedU2wdeHfoUhsQVb86dxI6kGdRPZbkHWf9xGHfNJPWd\n8QIu4RbOqZ3xc3L2rAtHizeBLFwixaNuhuA3OpXE5Yr/7p5INKAVKjRDtpWHQqBU\nFUqHyEQ3l+w2WuAwkHCKCMKtaqNaTKyAmy6+RRdPQ+kIWg4HKEzwc43YToKjgCwC\np249kdRZzB2dvJqM/uBt8Zh6h1b1+UlTGJRKxfQEPFY5dqLxZBomXaz4VNvyKfp2\ngneAVGaLMUthzaTR+T8w36yTodfPVGP+3kar3sbXi0Tblr4arqk5FJ7J6qzt7S+I\nr60r7aFtAgMBAAECggEABLv1J11q7oCuUomKX80LmtyKSC/V50LAJf0EanjsDFU0\nRii05OtVnTjZMY6meH7pqwxw4YBTsSOHO+VNRfp6c6sGJ4cGARv6tDgFqWE4C5UC\nIUXNxragmVzkbAV2fai7J7ScL+9U4HonsYIlZqPcYjlSx2O0/pMGIKSJu1iEWoxC\nD1+k/DpDdDFcBCEBkiOrQfgvY0CvXNjZ/tM2KHopMvVlREhnqVb5x0tvKDB8s3VU\nK6l1JF0vDak3txnXBeWMY1+b9S9Itb3ptHi85pYfAm5tD5EW9R5W+oA7AbUcKLkj\nmygkdCqC7pkb3vPqqMo4NUe7hGCkGI06jf9Bd8HjoQKBgQC5sX9jZeqqgtE1ERud\ndDQ0AKlAE/+OQoW5vNuaOhN2+KHj/GAmorrNZYOWvVLmIa1c1zx+op4CkLEHFvvL\ngvama/X0dXwIwln/AudsKnnA1GU5TBWJKHoYDDJs931Zdq07kn9hqV/XuZu8PezO\nLECMjcUN1jNRlMLSXWBpwWkBXQKBgQC4aNRYoY4q9/Qyj1RTa7Dk8BKOSL4jZG5n\n7wYMqsb3xaUmoJHSeVf7mt2KJBuQkPfrRVLOw8R0edxHNUqm5fLpVaOPJUhrU7lO\nrqi+e6cmV8biWekNybEHX+vv4B3i2vcjiNGACyniW3Yv0UjbDITZH6VYUh5/zcoO\nOw7d/GLPUQKBgGIuOhd4/IFZF3pCaGJw3WUdcF+D81vpSkExXL8Hs+D0hsw/VSs4\nYSJWaSPbSCiLZ9ktqDugiYD7tc301f79aKIHdQzizUjoUaMmiuvC7YsKAdcwpjZV\n43AxirvYgzs5J1DXHWiqoBU0euYlq7464YovLyAowAuDZxrI6kAgVf+1AoGAGFbt\nwA0CwLUdbBby4FfUb0Moj9MWFYHJ+LnZqI5Z2JYjqCeFV6xgansURolhggFAV7M8\nrMG2ClGTO2rTQZgUKav9/ITFPDU+vh3bc9jKRQtM2s9XLVSzou+MKosAJtMTz4Ld\nc/MFQjUkMkeDQDY0ypucrT2ZfPDifGJbIf2P5SECgYBbBIfRnTdd6gyHkk6Kl6I6\n0GU6fBc882Mny1YYOJ96UHjJY9k4fuJTetKSsCdoWPEY9QnaoY+Aya2Y8kbqflAH\nlCbJD4n0frDvaJOx5PL8sxIBvU6IiYHJzsEDALXUlQV5PA0fndztwo9Em+uXdBYr\nl8hDl28d18FUQM95PUBH+A==\n-----END PRIVATE KEY-----\n",
  "client_email": "edyodaa@edyoda-345516.iam.gserviceaccount.com",
  "client_id": "109266171020347379069",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/edyodaa%40edyoda-345516.iam.gserviceaccount.com"
}

gc= gspread.service_account_from_dict(credentials)


# In[19]:


sh=gc.open_by_url("https://docs.google.com/spreadsheets/d/1Y_g6LQI2GLqpKf-fj-rH7D9gfnP2MJzpFA6t0AsBMi8/edit#gid=0")


# In[20]:


sh.worksheets()


# In[21]:


worksheet = sh.get_worksheet_by_id(0)
worksheet2 = sh.get_worksheet_by_id(1548342679)


# In[22]:


class1 = pd.DataFrame(worksheet.get_all_records())
class2 = pd.DataFrame(worksheet2.get_all_records())


# In[23]:


class1['Type'].replace('','STUDENT',inplace=True)
class2['Type'].replace('','STUDENT',inplace=True)


# In[24]:


class1.set_index('Student Roll Num',inplace=True)
class2.set_index('Student Roll Num',inplace=True)


# In[25]:


class1_columns = list(class1.columns)
class1_columns.remove('Type')
class1_ratings = []
class1_dates = []
for i in class1_columns:
    if i.startswith('R'):
        class1_ratings.append(i)
    else:
        class1_dates.append(i)
        
class2_columns = list(class2.columns)
class2_columns.remove('Type')
class2_ratings = []
class2_dates = []
for i in class2_columns:
    if i.startswith('R'):
        class2_ratings.append(i)
    else:
        class2_dates.append(i)


# In[26]:


class1.replace('','Missed',inplace=True)


# In[27]:


def get_missed(row):
    try:
        return row.value_counts()['Missed']
    except:
        return 0
    
def get_attended(row):
    try:
        return row.value_counts()['Attended']
    except:
        return 0
    
def get_avg_rating(row):
    return row[class1_ratings].sum()/class1[class1_ratings].shape[1]


# In[28]:


class1['Total_Missed'] = class1.apply(get_missed,axis=1)
class1['Total_Attended'] = class1.apply(get_attended,axis=1)
class1['Avg_rating'] = class1.apply(get_avg_rating,axis=1)


# In[29]:


import plotly.express as px


# In[30]:


def need_attention(n):
    return class1.nlargest(n,columns='Total_Missed')[['Total_Missed']]
def unsatisfied_students(n):
    return class1.nsmallest(n,columns='Avg_rating')[['T']]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




