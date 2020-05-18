#Streaming and Saving (Pickle) with Notification - News
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


english_sources_twitter = {
    'ABC': '28785486',
    'abcnews': '2768501',
    'AJEnglish': '4970411',
    'arstechnica': '717313',
    'AssociatedPress': '49304503',
    'AP': '51241574',
    'FinancialReview': '19050000',
    'axios': '800707492346925056',
    'AxiosWorld': '952639892995047424',
    'BBCNews': '612473',
    'BBCSport': '265902729',
    'BleacherReport': '890891',
    'business': '34713362',
    'BreibartNews': '799004321702694917',
    'businessinsider': '20562637',
    'BIUK': '294176860',
    'BuzzFeed': '5695632',
    'CBCNews': '6433472',
    'CBSNews': '15012486',
    'CryptoCoinsNews': '1856523530',
    'MailOnline': '15438913',
    'DailyMailUK': '111556423',
    'DailyMailUS': '2744812164',
    'engadget': '14372486',
    'EW': '16312576',
    'espn': '2557521',
    'financialpost': '14216681',
    'FinancialTimes': '4898091',
    'FT': '18949452',
    'ftlive': '20152124',
    'FortuneMagazine': '25053299',
    'FourFourTwo': '34891363',
    'FourFourTwoUSA': '132335949',
    'FourFourTwoOz': '17461251',
    'FoxNews': '1367531',
    'foxnewsalert': '31540671',
    'FOXSports': '16877611',
    'googlenews': '33584794',
    'Independent': '16973333',
    'mashable': '972651',
    'mnt': '50340794',
    'MetroUK': '138749160',
    'DailyMirror': '16887175',
    'MSNBC': '2836421',
    'MTVNews': '40076725',
    'mtvuknews': '475950483',
    'NatGeo': '17471979',
    'NRO': '19417492',
    'NBCNews': '14173315',
    'News24': '14697575',
    'newscientist': '19658826',
    'newscomauHQ': '15250661',
    'Newsweek': '2884771',
    'NYMag': '45564482',
    'NFLNewsdesk': '336063029',
    'politico': '9300262',
    'Polygon': '454340464',
    'Recode': '2244340904',
    'Reuters': '1652541',
    'ReutersUK': '17038090',
    'rte': '1245699895',
    'talkSPORT': '15332636',
    'TechCrunch': '816653',
    'techradar': '15560223',
    'amconmag': '35511525',
    'TheEconomist': '5988062',
    'globeandmail': '8736882',
    'guardian': '87818409',
    'GuardianAus': '1092378031',
    'thehill': '1917731',
    'the_hindu': '20751449',
    'HuffPost': '14511951',
    'IrishTimes': '15084853',
    'ladbible': '331311644',
    'nytimes': '807095',
    'TheNextWeb': '10876852',
    'sportbible': '435225922',
    'Telegraph': '16343974',
    'TelegraphNews': '14138785',
    'timesofindia': '134758540',
    'verge': '275686563',
    'WSJ': '3108351',
    'washingtonpost': '2467791',
    'WashTimes': '14662354',
    'TIME': '14293310',
    'USATODAY': '15754281',
    'vicenews': '1630896181',
    'WIRED': '1344951',
    'WiredUK': '22363802',
    "NHSUK":"10215212",
    "Conservatives":"14281853",
    "UKLabour":"14291684",
    "LibDems":"5680622",
    "TheGreenParty":"15529670",
    "GovUK":"17481977",
    "sinnfeinireland":"22628924",
    "UUPOnline":"21090736",
    "Plaid_Cymru":"14411725",
    "TheSNP":"77821953"
    
}




#Creds
api_key="4bJdPa2TXN4bxfjb5pIZEc1bb"
api_seckey="ADSmYcwYBZViqvLTRJ8QsJ25AmgHcrZnXWWehGV8ec8TJq5zQY"

acc_tok="974952819223445505-RsewotYN1bOZyqxZfFAQKPvsCofXXN4"
acc_toksec="Ckz0NaB44kWOuxJaiwdxr7PXff0h1BtYguo1sOTNRHa9H"

count=0
over=0
flag=0

just_check=[]


#Classes and Functions

def from_creator(status):
    
    if hasattr(status, 'retweeted_status'):
        return False
    elif status.in_reply_to_status_id != None:
        return False
    elif status.in_reply_to_screen_name != None:
        return False
    elif status.in_reply_to_user_id != None:
        return False
    else:
        return True


class Listen(StreamListener):
    def __init__(self):
        super(Listen,self).__init__()

    def on_status(self,status):
        global count
        global over

        if from_creator(status):
            
                
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
            #print(status.author.name,"\t",text.replace("\n"," ").replace("\r"," "))
            #f.write(text.replace("\n"," ").replace("\r"," ")+"\n")
            #print()

        else:
            pass
        

    def on_error(self,stat_code):
        print(stat_code)
        if stat_code==420:
            emerg_stop()
            return False


def save_stream():
    global f
    dt=datetime.datetime.utcnow()
    f=open("news_data_"+str(dt.hour)+str(dt.minute)+str(dt.second)+".pickle","wb")
    #stream.sample(languages=["en"])
    stream.filter(follow=list(english_sources_twitter.values()),
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



