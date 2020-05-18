#Slot_Wise tweet
#Dict with key referring to the hour of tweet
#Values - Tweet_ID, User_ID, Tweet_Text, Porter, Snowball


from mysql.connector import connect
from pickle import load,dump


nf=open("Hourly_Slots.pickle","wb")

db=connect(host="proj-mysql.uopnet.plymouth.ac.uk",
			database="prco304_avarma",
			user="prco304_avarma",
			password="avarma_304")

c=db.cursor()

c.execute("select tweet_id,user_id,tweet_text,tweet_created_at,snowball,porter,hour(tweet_created_at) from tweet;")

d={}

count,over_ct=0,0


for i in c:

    if i[-1] not in d:
        d[i[-1]]=[tuple(i[:-1])]
    else:
        d[i[-1]].append(tuple(i[:-1]))

    count+=1

    if count>10000:
        over_ct+=1
        print(over_ct)
        count=0

dump(d,nf)
c.close()
db.close()
nf.close()


