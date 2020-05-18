#Streaming and Saving (Pickle) with Notification
#notify-run configure <channel_address>
#(without the c)
#Saving in the form [id,tweet_text]
#if needed, can recall tweet info using api.get_status(<tweet id>,tweet_mode="extended")


import sys
import tweepy
from tweepy.streaming import StreamListener
import pickle

from notify_run import Notify

ntf=Notify()
print(ntf.endpoint)

f=open("stream_test3.pickle","wb")
non_bmp_map=dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


#Creds
api_key="YIHxNkdYNGzrNdj0TPfFbnFmR"
api_seckey="BY2p6WVm0L5j4TV55l3Hj7tpexjIz6xeSjh676psFAYXRmuNqI"

acc_tok="974952819223445505-Hdiytd67IFrwtzUoZSKkJdFJbfjGUev"
acc_toksec="skAIgktED0hfVnVUsvhJyEAS5xDSX20HOocFFb0VUNT16"

count=0
over=0


#Classes and Functions
class Listen(StreamListener):
    def __init__(self):
        super(Listen,self).__init__()

    def on_status(self,status):
        global count
        global over

        if count<1000:
            count+=1
        else:
            count=0
            over+=1
            print("Done")
            ntf.send(str(over))
    
        #pickle.dump(status,f)
        
        if "retweeted_status" in dir(status):
            try:
                #print(status.retweeted_status.full_text.translate(non_bmp_map))
                text=status.retweeted_status.full_text
            except:
                #print(status.retweeted_status.text.translate(non_bmp_map))
                text=status.retweeted_status.text
                
        else:
            try:
                #print(status.full_text.translate(non_bmp_map))
                text=status.full_text
            except:
                #print(status.text.translate(non_bmp_map))
                text=status.text

        pickle.dump([status.id,text],f)
        #print()
        

    def on_error(self,stat_code):
        print(stat_code)
        return False

  
#Connect with Twitter
#auth=tweepy.AppAuthHandler(api_key,api_seckey)
auth=tweepy.OAuthHandler(api_key,api_seckey)
auth.set_access_token(acc_tok,acc_toksec)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

listen=Listen()
stream=tweepy.Stream(auth=api.auth,listener=listen)


try:
    api.verify_credentials()
    print("Verified")
    ntf.send("Verified Creds")
    
    print("Starting Streaming")
    ntf.send("Starting Streaming")
    stream.sample(languages=["en"])
    #stream.filter(track=['coronavirus','CoronaVirusOutbreak'],languages=['en'])
    
except KeyboardInterrupt:
    print("Stopping Stream")
    ntf.send("Keyboard Interrupt")

except:
    print("Unknown Error")
    ntf.send("Unknown Error")
    

finally:
    print("Stopped Stream")
    ntf.send("Stopped Stream")
    ntf.send(str(count))
    f.close()
    stream.disconnect()



