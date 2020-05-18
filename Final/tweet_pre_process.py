#Tweet Pre-Processing
#Read tweet dict file and remade new file with
#pre_processed text field after stopwords.

#Using TweetTokenizer class for tokenizing the tweets after lower case.


from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer


from pickle import load,dump



f=open("NFL_Complete_V7.pickle","rb")
nf=open("NFL_Complete_V6_Pre_Processed.pickle","wb")


l_sw=stopwords.words("english")
tk=TweetTokenizer()

porter=PorterStemmer()

snow=SnowballStemmer("english")


count=0
over_ct=0

while 1:

    if count==10000:
        over_ct+=1
        print(over_ct)
        count=0
    try:
        a=load(f)
        a_copy=dict(a)
        tokens=tk.tokenize(a_copy["tweet_text"].lower())
        
        fl=[]
        for i in tokens:
            if i not in l_sw:
                fl.append(i)

        port_tweet=[porter.stem(i) for i in fl]
        snow_tweet=[snow.stem(i) for i in fl]

        a["porter"]=port_tweet
        a["snowball"]=snow_tweet
        a["tokens"]=tokens

        dump(a,nf)
        count+=1
        
        #print("\n\n",a["tweet_text"])
        #print(a["tweet_id"])
        #print(tokens)
        #print(port_tweet)
        #print(snow_tweet)
    except EOFError:
        print("Done")
        break

print(count)

    


        
        
        

        
                
