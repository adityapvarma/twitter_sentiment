##Generic Graph - Bar NSR S140

#y=[0,45150,45982,46702,49296,46565,45595,44267,42445,41231,2528]
#y=[0,193,219,197,219,199,208,196,191,149,0]

import numpy as np
nan=np.nan
v_tr=[-1.0, 0.10952380952380952, -1.0, 0.0, 0.0136986301369863, 0.08004533541120634, 1.0, 0.0, 0.05781714903976197, 0.0, 0.043478260869565216, 0.06267084472298153, 0.0, 0.05574324324324324, 0.07257226034518612, 0.0, 0.0, 0.0, 0.06500505220613001, 0.0, 0.07377049180327869, 0.008333333333333333, 0.0, -1.0, 0.07537792503623938, 0.0, 0.0, 0.09281437125748503, -0.2527075812274368, 0.0, 0.06340464590835275, 0.004608294930875576, 0.0, 0.0770439222360411, 0.0, 0.0, 1.0, 0.07943431139307428, 0.0, 0.058333333333333334, 0.08359931254603487, 0.0, 0.0, 0.0659264399722415, 0.0, 0.08588957055214724, -0.7383177570093458, 0.0, 0.0, 0.06737869198312237, 0.0, -0.6705882352941176, 0.06318836931210271, 0.0, 0.0, 0.0, -0.6694214876033058, 0.10465116279069768, 0.0, 0.0, 0.05714285714285714, 0.10843373493975904, 0.06765297328353921, 0.0, 0.0, 0.07354758961681088, -0.36585365853658536, 0.0, 0.0, 0.03260869565217391, 0.06159322944653412, 0.0, 0.0, 0.013157894736842105, 0.08583690987124463, 0.0, 1.0, -0.7974683544303798, 0.050314465408805034, 0.0, 0.07781823374027272, 0.0, -1.0, 0.06946317777178311, -1.0, 0.0, 0.0, 0.04411764705882353, 0.04771232685042675, -1.0, 0.06810035842293907, 0.0, 0.0, 0.046875, 0.08484848484848485, 0.042695626301695926, -1.0, 0.0, 0.06805293005671077, 0.10144927536231885, -1.0, 0.05292708489294805, 0.0, 0.06995230524642289, 0.05503864872602347, 0.08843537414965986, 0.05217391304347826, -0.5116279069767442, 0.059778218403466254, 0.0, -0.5508474576271186, 0.06591351189585515, -0.6859504132231405, 0.0, 0.08231173380035026, 0.06305747304739005, 0.0, 0.023809523809523808, 0.05454133977066988, 0.0, 0.0, 0.04733947681331748, 0.16546762589928057, 0.2, 0.0, 0.04486062717770035]
v_conf1=[nan, 0.08, nan, nan, 0.02, 0.15, nan, nan, 0.14, nan, 0.07, 0.13, nan, 0.08, 0.14, nan, nan, nan, 0.13, nan, 0.15, nan, nan, nan, 0.14, nan, nan, 0.18, -0.12, nan, 0.14, nan, nan, 0.12, nan, nan, nan, 0.13, nan, 0.25, 0.14, nan, nan, nan, nan, 0.11, nan, nan, nan, 0.14, nan, nan, 0.15, nan, nan, nan, nan, 0.08, nan, nan, 0.11, 0.04, 0.15, nan, nan, 0.15, nan, nan, nan, 0.04, 0.15, nan, nan, -0.02, 0.15, nan, nan, nan, 0.13, nan, 0.17, nan, nan, 0.15, nan, nan, nan, 0.11, 0.12, nan, 0.1, nan, nan, 0.05, 0.03, 0.13, nan, nan, 0.13, -0.16, nan, 0.14, nan, 0.15, 0.16, 0.1, 0.19, nan, 0.14, nan, nan, 0.15, nan, nan, 0.19, 0.15, nan, nan, 0.12, nan, nan, 0.14, 0.17, 0.23, nan, nan]
x=[i for i in range(len(v_tr))]
v_conf=[]

import math

v_tr_mod=[]
from copy import deepcopy

for i in range(len(v_conf1)):
    if math.isnan(v_conf1[i]):
        v_tr_mod.append(deepcopy(v_tr[i]))
        v_conf.append(np.nan)
    else:
        v_tr_mod.append(np.nan)
        v_conf.append(deepcopy(v_tr[i]))


import matplotlib.pyplot as plt

limitt=[]
for i in v_conf:
    if not math.isnan(i):
        limitt.append(deepcopy(i))


plt.rcParams.update({'font.size': 16})


#xlabel=['14:24'," "," ",'14:54'," "," ",'15:24'," "," ",'15:54'," "," ",'16:24'," "," ",'16:54'," "," ",'17:24'," "," ",'17:54'," "," ",'18:24'," "," ",'18:54'," "," ",'19:24']
fig, ax = plt.subplots()
ax.plot(x,v_tr_mod,'go',label="Potential Trending Cluster")
#ax.plot(x,y1,"go")
ax.plot(x,v_conf,'r^',label="Trending Cluster")
#ax.plot(x,y2,"bo")
#ax.grid(linestyle='--')
#plt.xlabel("Time (GMT -1)", labelpad=18)
plt.ylabel("NSR",labelpad=18)
#plt.xticks(x,xlabel,rotation=90)

from matplotlib.ticker import FormatStrFormatter
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.yaxis.set_ticks(np.arange(-1, 1.25, 0.25))

handles, labels1 = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels1[::-1], loc='upper left')

ax.get_xaxis().set_visible(False)

max_val="{:0.2f}".format(max(limitt))
min_val="{:0.2f}".format(min(limitt))

ax.axhline(y=max(limitt),ls="--",color="b")
ax.text(0,max(limitt)+0.02,max_val,color="b",size=14)

ax.axhline(y=min(limitt),ls="--",color="b")
ax.text(0,min(limitt)-0.07,min_val,color="b",size=14)



plt.show()
