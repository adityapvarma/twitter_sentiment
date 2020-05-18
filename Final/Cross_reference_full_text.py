##CrossCheck adn resave
import pickle

f1=open("NFL_Complete_V6.pickle","rb")


nf=open("NFL_Complete_V7.pickle","wb")
count=0
over_ct=0
while 1:
    if count==10000:
        over_ct+=1
        count=0
        print(over_ct)

    try:
        a=pickle.load(f1)
        f2=open("nfl_consolidated.pickle","rb")
        while 1:
            try:
                b=pickle.load(f2)
                if a["tweet_id"]==b[0]:
                    a["tweet_text"]=b[1]
                    pickle.dump(a,nf)
                    count+=1
                    f2.close()
                    break
                
            except EOFError:
                print("Error Tweet not found! ID :",a["tweet_id"])
                f2.close()
    except EOFError:
        print("Done")
        break

f1.close()
f2.close()
nf.close()
        
        
                
                
