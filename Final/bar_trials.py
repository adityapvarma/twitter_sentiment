#Bar Stack

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

plt.rcParams.update({'font.size': 18})

xt=['Sentiment140','SentiStrength','Treebank','uClassify','VADER']

pos=np.array([9285,16224,5739,31323,4548])
neg=np.array([439,5684,27505,2396,274])
neu=np.array([31188,19004,7668,7193,36090])

yfinal=np.vstack((pos,neg,neu))
x=[i for i in range(5)]

fig,ax=plt.subplots()
#ax.bar(x,yfinal,0.35)
a1=ax.bar(x,pos,0.5,color='g')
a2=ax.bar(x,neg,0.5,bottom=pos,color='r')
a3=ax.bar(x,neu,0.5,bottom=pos+neg,color='#FFBF00')
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
plt.xticks(x,xt)
fig.legend((a3[0], a2[0], a1[0]), ('Neutral', 'Negative', 'Positive'),ncol=4,loc='lower center')
#plt.xlabel("Tools", labelpad=18)
plt.ylabel("Number of tweets",labelpad=18)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.show()


#,colors=['g','r','#FFBF00']
