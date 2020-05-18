#Stack Plot
#Hourly Sentiment General

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from pickle import load,dump

#plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 24})

f=open("csa_mod_Sentiment_Hourly.pickle","rb")
senti=load(f)

xt=["21:47","22:47","23:47","0:47",
    "1:47","2:47","3:47","4:47",
    "5:47","6:47","7:47","8:47","9:47"]

ystk=[{"pos":0,"neg":0,"neu":0}]
i=0

for i in xt:
    temp=deepcopy(ystk[-1])
    for k in senti[i]:
        temp[k]+=senti[i][k]

    ystk.append(temp)
xt=["20:47"]+xt

        
    
pos=[i["pos"] for i in ystk]
neg=[i["neg"] for i in ystk]
neu=[i["neu"] for i in ystk]

yfinal=np.vstack((neg,neu,pos))
x=[i for i in range(14)]

labels=["Negative","Neutral","Positive"]
fig, ax = plt.subplots()
ax.stackplot(x,yfinal, labels=labels,colors=['r','#FFBF00','g'])
plt.xticks(x,xt,rotation=90)
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
ax.legend(loc='upper left')
ax.grid(True)
plt.xlabel("Time (GMT)", labelpad=18)
plt.ylabel("Number of tweets",labelpad=18)

handles, labels1 = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels1[::-1], loc='upper left')

plt.show()
