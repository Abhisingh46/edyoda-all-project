#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().system('pip install tweepy')
get_ipython().system('pip install geocoder')


# In[13]:


import tweepy
import pandas as pd
import geocoder


# In[44]:


consumer_key="mx5EJBuHZK2gaMm8FtuPhx0Rf"
consumer_secret="cZHZeSTebSSkDAmLpYA9YzF9U77JtsbWdNiaDi18ecsMq4Flw0"
access_token="4500086892-BUcwnowx8QfEpBbG6ks0UXG1KrVs8kFRqbdDTAQ"
access_token_secret="ZNQbCKYiYrb1b0404tWDHoLQUTsebMYx10OYUzULpAGhO"


# In[45]:


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth) #calling the api


# In[46]:


# WOEID of INDIA
woeid = 23424848
 
# getting the trends
trends = api.get_place_trends(id = woeid, exclude = "hashtags")
print("The top trends for the location are :")
for value in trends:
    for trend in value['trends']:
        print(trend['name'])


# # ANALYSIS OF TWEETS

# In[47]:


get_ipython().system('pip install textblob')
get_ipython().system('pip install pycountry')


# In[48]:


from textblob import TextBlob
import sys
import matplotlib.pyplot as plt
import numpy as np
import os
import nltk
import pycountry
import re
import string


# In[49]:


from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer


# In[54]:


import nltk
nltk.downloader.download('vader_lexicon')


# In[57]:


def percentage(part,whole):
    return 100 * float(part)/float(whole)

keyword = input("Please enter keyword or hashtag to search: ")
noOfTweet = int(input ("Please enter how many tweets to analyze: "))
tweets = tweepy.Cursor(api.search_tweets,q=keyword).items(noOfTweet)
positive = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []

for tweet in tweets:
#print(tweet.text)
    tweet_list.append(tweet.text)
    analysis = TextBlob(tweet.text)
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score['compound']
    polarity += analysis.sentiment.polarity

    if neg > pos:
        negative_list.append(tweet.text)
        negative += 1
    elif pos > neg:
        positive_list.append(tweet.text)
        positive += 1
    elif pos == neg:
        neutral_list.append(tweet.text)
        neutral += 1
positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)

positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')


# In[58]:


#Number of Tweets (Total, Positive, Negative, Neutral)
tweet_list = pd.DataFrame(tweet_list)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)
print("total number: ",len(tweet_list))
print("positive number: ",len(positive_list))
print("negative number: ", len(negative_list))
print("neutral number: ",len(neutral_list))


# # Visualization

# In[59]:


#Pie chart of positive, negative, neutral tweets


# In[60]:


labels = ['Positive ['+str(positive)+'%]' , 'Neutral ['+str(neutral)+'%]','Negative ['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'blue','red']
patches, texts = plt.pie(sizes,colors=colors, startangle=90)
plt.style.use('default')
plt.legend(labels)
plt.title("Sentiment Analysis Result for keyword= "+keyword+"" )
plt.axis("equal")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




