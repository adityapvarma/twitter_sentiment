#Labelling dataset
from pickle import load,dump
from copy import deepcopy


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def serial(s):
    temp=''
    for i in s:
        temp+=(i+" ")

    return temp[:-1]


vader=SentimentIntensityAnalyzer()

fc={"pos":0,
    "neg":0,
    "neu":0}

common_fc={"tweet_text":deepcopy(fc),
           "porter":deepcopy(fc),
           "snowball":deepcopy(fc)
           }


#Read file and aggregate into a list of dict l
pickle
and load into l


for i in l:
    temp={}
    lb1="none"
    lb=vader.polarity_scores(i["tweet_text"])

    if lb["compound"]>=0.5:
        lb1=1
    elif lb["compound"]<=-0.5:
        lb1=-1
    else:
        lb1=0

    for j in i:
        temp[j]=i[j]
    temp["label"]=lb1

        
    
