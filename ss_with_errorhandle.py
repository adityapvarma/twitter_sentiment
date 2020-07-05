#Streaming and Saving (Pickle) with Notification
#notify-run configure <channel_address>
#(without the c)
#Saving in the form [id,tweet_text]
#if needed, can recall tweet info using api.get_status(<tweet id>,tweet_mode="extended")


import sys
import tweepy
from tweepy.streaming import StreamListener
import pickle
import datetime

from notify_run import Notify

ntf=Notify()
print(ntf.endpoint)

#f=open("stream_test3.pickle","wb")
f=0
non_bmp_map=dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


#Creds
api_key=""
api_seckey=""

acc_tok=""
acc_toksec=""

count=0
over=0
flag=0

just_check=[]


#Classes and Functions
class Listen(StreamListener):
    def __init__(self):
        super(Listen,self).__init__()

    def on_status(self,status):
        global count
        global over

        #global just_check
        #just_check.append(status)

        if count<10000:
            count+=1
        else:
            count=0
            over+=1
            print(over," Done")
            ntf.send(str(over))
    
        #pickle.dump(status,f)
        #print(count,end= "  ")
        if "retweeted_status" in dir(status):
            try:
                #print(status.retweeted_status.extended_tweet["full_text"].translate(non_bmp_map))
                #print("              In")
                text=status.retweeted_status.extended_tweet["full_text"]
                
            except:
                #print(status.retweeted_status.text.translate(non_bmp_map))
                text=status.retweeted_status.text


        else:

            try:
                
                #print(status.extended_tweet["full_text"].translate(non_bmp_map))
                #print("              In")
                text=status.extended_tweet["full_text"]
                
            except:
                #print(status.text.translate(non_bmp_map))
                text=status.text


        dct={
            "tweet_id":status.id,
            "tweet_text":text,
            "tweet_created_at":status.created_at,
            "user_id":status.author.id
            }
                

        pickle.dump(dct,f)
        #f.write(text.replace("\n"," ").replace("\r"," ")+"\n")
        #print()
        

    def on_error(self,stat_code):
        print(stat_code)
        if stat_code==420:
            emerg_stop()
            return False


def save_stream():
    global f
    dt=datetime.datetime.utcnow()
    f=open("corona_data_"+str(dt.hour)+str(dt.minute)+str(dt.second)+".pickle","wb")
    #stream.sample(languages=["en"])
    stream.filter(track=["#covid19","#covid_19","#covid-19","#coronavirusoutbreak","#covid2019","#Coronavirus",
                         "#SARSCoV2","#virus","#SocialDistancing","#stayhome","#flattenthecurve"],
                  languages=['en'])
    
def emerg_stop():
    global flag
    flag=1
    print("420 Stopped Stream")
    ##ntf.send("420 Stopped Stream")
    #ntf.send(str(count))
    #f.close()
    #stream.disconnect()
    
    
    
    

  
#Connect with Twitter
#auth=tweepy.AppAuthHandler(api_key,api_seckey)
auth=tweepy.OAuthHandler(api_key,api_seckey)
auth.set_access_token(acc_tok,acc_toksec)

#auth=tweepy.AppAuthHandler(api_key,api_seckey)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

listen=Listen()
stream=tweepy.Stream(auth=api.auth,listener=listen)

while 1:
    
    try:
        
        api.verify_credentials()
        print("Verified")
        #ntf.send("Verified Creds")
        
        print("Starting Streaming")
        #ntf.send("Starting Streaming")
        save_stream()
        #stream.sample(languages=["en"])
        #stream.filter(track=['coronavirus','CoronaVirusOutbreak'],languages=['en'])
        
    except KeyboardInterrupt:
        print("Stopping Stream")
        #ntf.send("Keyboard Interrupt")
        break

    except:
        print("Unknown Error, Restarting")
        #ntf.send("Unknown Error, Restarting")
        

    finally:
        print("Stopped Stream")
        #ntf.send("Stopped Stream")
        #ntf.send(str(count))
        #f.close()
        stream.disconnect()
        if flag:
            break

f.close()
#ntf.send("Program Halted!!!")



