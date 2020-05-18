##Generic Graph - Bar NSR S140

#y=[0,45150,45982,46702,49296,46565,45595,44267,42445,41231,2528]
#y=[0,193,219,197,219,199,208,196,191,149,0]

import numpy as np
nan=np.nan
v_tr=[-1.0, -0.23809523809523808, -1.0, 0.0, -0.1643835616438356, -0.15074024226110364, 0.0, -1.0, -0.1591831214498242, -1.0, -0.2463768115942029, -0.175745049669978, -1.0, -0.20608108108108109, -0.1596312469674915, -1.0, -1.0, 1.0, -0.16369147861232738, -1.0, -0.21475409836065573, 0.008333333333333333, 1.0, -1.0, -0.18071374335611237, 0.01764705882352941, -1.0, -0.23952095808383234, -0.3104693140794224, 0.0, -0.17503353809221212, 0.004608294930875576, 0.0, -0.18164561104928978, 0.0, 0.0, -0.9841269841269841, -0.16230504890298705, 0.0, -0.10833333333333334, -0.17566904001964154, 0.0, 0.0, -0.15803419342628225, 0.0, -0.2167689161554192, -1.0, -1.0, 0.0, -0.16363396624472573, 0.0, -1.0, -0.17238340990622444, 0.0, -1.0, 0.0, -1.0, -0.22093023255813954, -1.0, -1.0, -0.18571428571428572, -0.16265060240963855, -0.16252513645504166, 0.0, 1.0, -0.15025408597720094, -1.0, -1.0, 0.0, -0.2826086956521739, -0.16100214938205265, 0.0, 0.0, -0.32894736842105265, -0.08583690987124463, -1.0, 0.0, -1.0, -0.16352201257861634, -1.0, -0.1453558934818305, -1.0, -1.0, -0.15720258969517129, -1.0, 0.0, -1.0, -0.19669117647058823, -0.17279977612984468, -1.0, -0.26344086021505375, 0.0, -1.0, -0.17578125, -0.2909090909090909, -0.16498066051770308, 1.0, 0.0, -0.2684310018903592, -0.18115942028985507, -1.0, -0.16828866596795927, -1.0, -0.2480127186009539, -0.13505582593758947, -0.272108843537415, -0.07391304347826087, 0.0, -0.1539252405081883, 0.9881656804733728, 0.0, -0.15120454885530452, 0.0, 1.0, -0.18213660245183888, -0.13751648181183587, -1.0, -0.2857142857142857, -0.14046469523234761, -1.0, -1.0, -0.13540428061831153, -0.302158273381295, -0.1, -0.30303030303030304, -0.14590592334494773]
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
