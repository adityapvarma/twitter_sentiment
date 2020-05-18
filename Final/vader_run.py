#VADER

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pickle import load,dump
import emojis
from copy import deepcopy




def serl(lt):
    
    temp=''
    for i in lt:
        temp+=(i+" ")
    
    return emojis.encode(temp)

vader_ob = SentimentIntensityAnalyzer()

fc={"pos":0,
    "neg":0,
    "neu":0}

common_fc={"tweet_text":deepcopy(fc),
           "porter":deepcopy(fc),
           "snowball":deepcopy(fc)
           }


#Maintain an fc for text, porter and snowball

#Aggregate dict from VADER_Files into a list of dict
f=open("VADER_Files.pickle","rb")
nf=open("Post_VADER_Trials.pickle","wb")
lt_d=[]

while 1:
    try:
        a=load(f)
        lt_d.append(a)
    except EOFError:
        break
print("Done Loading")

#Iterate over lt_d and run VADER on all 3 fields
#Save the results in another file.
print("Starting VADER Run")
print()

count=0
over_ct=0


for i in lt_d:
    temp={}
    ref1=["tweet_id","user_id"]
    ref2=["tweet_text","snowball","porter"]

    for j in ref1:
        temp[j]=i[j]
    for j in ref2:
        if isinstance(i[j],list):
            temp[j]=vader_ob.polarity_scores(serl(i[j]))

        else:
            temp[j]=vader_ob.polarity_scores(i[j])
            
        if temp[j]["compound"]>=0.05:
            common_fc[j]["pos"]+=1
        elif temp[j]["compound"]<=-0.05:
            common_fc[j]["neg"]+=1
        else:
            common_fc[j]["neu"]+=1

    dump(temp,nf)

    count+=1
    if count>10000:
        over_ct+=1
        print(over_ct)
        count=0

f.close()
nf.close()

print("Final Count :")

for i in common_fc:
    print(i)
    for j in common_fc[i]:
        print(j," : ",common_fc[i][j])
    print()
    
    
    
        


