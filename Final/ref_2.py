#Cross Ref 2

import pickle
f1=open("NFL_Complete_V6.pickle","rb")
f2=open("nfl_consolidated.pickle","rb")

nf=open("NFL_Complete_V7.pickle","wb")
count=0
over_ct=0

d={}

#Load data
while 1:
    try:
        a=pickle.load(f2)
        d[a[0]]=a[1]
    except EOFError:
        print("Done Loading")
        f2.close()
        break

while 1:
    if count==10000:
        over_ct+=1
        count=0
        print(over_ct)
    try:
        a=pickle.load(f1)
        a["tweet_text"]=d[a["tweet_id"]]
        pickle.dump(a,nf)
        count+=1
    except EOFError:
        print("Done")
        f1.close()
        break

nf.close()


        
    
