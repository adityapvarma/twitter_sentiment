#Convert Consolidated dict file into txt file with delimiter ||

import pickle
import emojis

f=open("NFL_Complete_V7.pickle","rb")
nf=open("NFL_Complete_textV2.txt","w",encoding="utf-8")

buff=0
count=0
over_ct=0

lt=[
	"tweet_id","tweet_text","tweet_hashtags",
	"tweet_created_at","tweet_coordinates","tweet_fav_count",
	"tweet_source","tweet_rt_status","tweet_rt_count",
	"user_id","user_name","user_screen","user_created_at",
	"user_follower_count","user_geo_status","user_location"]

while 1:
    if count==10000:
        count=0
        over_ct+=1
        print(over_ct)
    try:
        a=pickle.load(f)

        for i in lt[:-1]:
            buff=nf.write(emojis.decode(str(a[i]))+"||")
            #buff=nf.write(emojis.decode(str(a[i]))+"||")

        buff=nf.write(emojis.decode(str(a[lt[-1]]))+"\n")
        count+=1

    except EOFError:
        print("Done")
        print(count)
        break

nf.close()
f.close()


        
        
        
