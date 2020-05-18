#Querying and collecting the other info required using statuses_lookup(<list of ids>,tweet_mode="extended")
#if needed, can recall tweet info using api.get_status(<tweet id>,tweet_mode="extended")

import tweepy
import sys
from time import sleep
import pickle


non_bmp_map=dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


#Creds Personal
api_key="YIHxNkdYNGzrNdj0TPfFbnFmR"
api_seckey="BY2p6WVm0L5j4TV55l3Hj7tpexjIz6xeSjh676psFAYXRmuNqI"


acc_tok="974952819223445505-Hdiytd67IFrwtzUoZSKkJdFJbfjGUev"
acc_toksec="skAIgktED0hfVnVUsvhJyEAS5xDSX20HOocFFb0VUNT16"

#New Creds
#api_key="loInnSkEuqhNNATrISRJ2CSHi"
#api_seckey="Qt2RYJjk54lFKgvUphSvjw8vmh7Axgjn7JnOZwWC15G2KQjhiw"


#Connect with Twitter
auth=tweepy.AppAuthHandler(api_key,api_seckey)
#auth=tweepy.OAuthHandler(api_key,api_seckey)
#auth.set_access_token(acc_tok,acc_toksec)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#Include a filter for english language check 
def get_dat(lt):

    #d=api.get_status(a[0],tweet_mode="extended")
    d=api.statuses_lookup(lt)

    l_dc=[]

    for j in d:

        hashes=[]

        if j.entities["hashtags"]:
            for i in j.entities["hashtags"]:
                hashes.append(i['text'])
        else:
            hashes=[]

        a=[]

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
        


        dct={
            "tweet_id":a[0],
            "tweet_text":a[1],
            "tweet_hashtags":hashes,
            "tweet_created_at":j.created_at,
            "tweet_coordinates":j.coordinates,
            "tweet_fav_count":j.favorite_count,
            "tweet_source":j.source,
            "tweet_rt_status":hasattr(j,"retweeted_status"),
            "tweet_rt_count":j.retweet_count,
            "user_id":j.author.id,
            "user_name":j.author.name,
            "user_screen":j.author.screen_name,
            "user_created_at":j.author.created_at,
            "user_follower_count":j.author.followers_count,
            "user_geo_status":j.author.geo_enabled,
            "user_location":j.author.location
            }
        l_dc.append(dct)
        #print("End")

    

    return l_dc


    
"""
            
        
    lt=[
        a[0],
        a[1],
        hashes,
        d.created_at,
        d.coordinates,
        d.favorite_count,
        d.source,
        hasattr(d,"retweeted_status"),
        d.retweet_count,
        d.author.id,
        d.author.name,
        d.author.screen_name,
        d.author.created_at,
        d.author.followers_count,
        d.author.followers_ids(),
        d.author.geo_enabled,
        d.author.location]

Pending cursor "user_follower_ids":j.author.followers_ids(),
"""   


        #print("Done")
"""
        f_list=[]

        if j.author.followers_count>=5000:
            
            for page in tweepy.Cursor(api.followers_ids,screen_name=j.author.screen_name).pages():
                f_list.extend(page)
                #print(len(page))
                sleep(30)
        else:
            for page in tweepy.Cursor(api.followers_ids,screen_name=j.author.screen_name).pages():
                f_list.extend(page)
                
                
            
"""            

        #print("F Done")
        #print(len(f_list))

     

    
        


#Info to be queried and Collected
#Tweet ID : a[0]
#Tweet Text (Extended) : a[1]
#Tweet Hashtags : inside d.entities
#Tweet Date and Time : d.created_at
#Tweet Location : d.coordinates
#Tweet Liked/favorite count :d.favorite_count
#Tweet Source : d.source
#Tweet Re-tweeted status: hasattr(d,"retweeted_status")
#Tweet re_tweeted count : d.retweet_count (inside if?)

#User ID : d.author.id
#User Name : d.author.name
#User Screenname : d.author.screen_name
#User Account creation date : d.author.created_at
#User Follower count : d.author.followers_count
#User follower IDs : d.author.followers_ids()
#User Geo-Enabled (Bool) : d.author.geo_enabled
#User location : d.author.location


