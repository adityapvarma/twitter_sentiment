#Querying and collecting the other info required.
#if needed, can recall tweet info using api.get_status(<tweet id>,tweet_mode="extended")

import tweepy
import sys
from time import sleep

non_bmp_map=dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


#Creds
api_key="YIHxNkdYNGzrNdj0TPfFbnFmR"
api_seckey="BY2p6WVm0L5j4TV55l3Hj7tpexjIz6xeSjh676psFAYXRmuNqI"

acc_tok="974952819223445505-Hdiytd67IFrwtzUoZSKkJdFJbfjGUev"
acc_toksec="skAIgktED0hfVnVUsvhJyEAS5xDSX20HOocFFb0VUNT16"

#Connect with Twitter
#auth=tweepy.AppAuthHandler(api_key,api_seckey)
auth=tweepy.OAuthHandler(api_key,api_seckey)
auth.set_access_token(acc_tok,acc_toksec)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def get_dat(a):

    d=api.get_status(a[0],tweet_mode="extended")

    hashes=[]

    if d.entities["hashtags"]:
        for i in d.entities["hashtags"]:
            hashes.append(i['text'])
    else:
        hashes=[]
 

    dct={
        "tweet_id":a[0],
        "tweet_text":a[1],
        "tweet_hashtags":hashes,
        "tweet_created_at":d.created_at,
        "tweet_coordinates":d.coordinates,
        "tweet_fav_count":d.favorite_count,
        "tweet_source":d.source,
        "tweet_rt_status":hasattr(d,"retweeted_status"),
        "tweet_rt_count":d.retweet_count,
        "user_id":d.author.id,
        "user_name":d.author.name,
        "user_screen":d.author.screen_name,
        "user_created_at":d.author.created_at,
        "user_follower_count":d.author.followers_count,
        "user_follower_ids":d.author.followers_ids(),
        "user_geo_status":d.author.geo_enabled,
        "user_location":d.author.location
        }

    return dct


    
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
"""   




    
        

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


