# -*- coding: utf-8 -*-
"""Custom_Classifier_Dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b5pN09Mqx_leFoKGtOVVkcUcarOGIkuD

Collect and Aggregate old dataset 
Data to be Collected

Tweet ID,
Tweet Text,
"""

import pandas as pd
df=pd.read_csv("Old_Dataset/tweets.nfl.2012.postgame.csv",header=None)

l=list(df.get(0))

final_list=[]

import tweepy
import sys
from time import sleep
from pickle import dump

from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import nltk
nltk.download('stopwords')

#Creds Personal
#api_key="YIHxNkdYNGzrNdj0TPfFbnFmR"
#api_seckey="BY2p6WVm0L5j4TV55l3Hj7tpexjIz6xeSjh676psFAYXRmuNqI"

api_key="loInnSkEuqhNNATrISRJ2CSHi"
api_seckey="Qt2RYJjk54lFKgvUphSvjw8vmh7Axgjn7JnOZwWC15G2KQjhiw"


acc_tok="974952819223445505-Hdiytd67IFrwtzUoZSKkJdFJbfjGUev"
acc_toksec="skAIgktED0hfVnVUsvhJyEAS5xDSX20HOocFFb0VUNT16"

auth=tweepy.AppAuthHandler(api_key,api_seckey)
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def get_dat(lt):

  #d=api.get_status(a[0],tweet_mode="extended")
  d=api.statuses_lookup(lt)
  l_dc=[]

  l_sw=stopwords.words("english")
  tk=TweetTokenizer()
  snow=SnowballStemmer("english")

  for j in d:

    a=[]
    if j.lang=='en':

      if "retweeted_status" in dir(j):
        try:
          text=j.retweeted_status.extended_tweet["full_text"]
        except:
          text=j.retweeted_status.text

      else:
        try:
          text=j.extended_tweet["full_text"]
        except:
          text=j.text

      a=[j.id,text]
      
      tokens=tk.tokenize(a[1].lower())
      
      fll=[]
      for k in tokens:
        if k not in l_sw:
          fll.append(k)
      
      snowl=[snow.stem(i) for i in fll]

      dct={
          "tweet_id":a[0],
          "tweet_text":a[1],
           "snow":snowl
          }
      l_dc.append(dct)
      #print("End")

  return l_dc

from pickle import dump

i=0
temp=[]
flag=0
rc=0

while 1:
  try:
    temp.append(l[i])
    i+=1
  except:
    flag=1
  
  if len(temp)==100:
    temp2=get_dat(temp)
    final_list.extend(temp2)
    rc+=1
    temp=[]
    
  if rc==500:
    print("Check")
    rc=0

  if flag:
    break

final_list.extend(get_dat(temp))

nf=open("Dataset_Raw_2.pickle","wb")
dump(final_list,nf)
nf.close()

len(final_list)
