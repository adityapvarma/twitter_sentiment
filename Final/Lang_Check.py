import tweepy
import sys
from time import sleep
from pickle import dump
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

    for j in d:
        if j.lang=='en':
            l_dc.append(d[0].id)
    
    #l_dc.append(dct)
    #print("End")

    return l_dc
    
