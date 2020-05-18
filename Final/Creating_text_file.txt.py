
import sys
import pickle
import json
#import pandas as pd
import csv
import re #regular expression
#from textblob import TextBlob
import string

f=open('Sentiment_DatasetV2.pickle','rb')
fb=open('Senti_Snow.txt','w',encoding="utf-8")


count=0     
while 1:
    try:
        a=pickle.load(f)
        fb.write(str(a["tweet_id"])+"\t"+a["snowball"].replace("\n"," ").replace("\r"," ")+'\n')
        count+=1
    except EOFError:
        flag=0
        break

f.close()
fb.close()
 
    
