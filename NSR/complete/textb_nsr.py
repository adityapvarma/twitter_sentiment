##Generic Graph - Bar NSR S140

#y=[0,45150,45982,46702,49296,46565,45595,44267,42445,41231,2528]
#y=[0,193,219,197,219,199,208,196,191,149,0]

import numpy as np
nan=np.nan
v_tr=[-1.0, 0.319047619047619, 1.0, 1.0, 0.3059360730593607, 0.34787844442870297, 1.0, -1.0, 0.3545442250473357, -1.0, 0.37681159420289856, 0.3539569304620308, 1.0, 0.33952702702702703, 0.3526720731960907, 1.0, 0.0, 1.0, 0.3351970360390704, 1.0, 0.33934426229508197, 0.975, 1.0, -1.0, 0.3344377717954028, 0.011764705882352941, 1.0, 0.38173652694610777, 0.6245487364620939, 0.0, 0.3321330226646897, 0.0, 1.0, 0.3339006349414152, 0.0, 0.0, 0.007936507936507936, 0.3400079302141158, 0.005847953216374269, 0.30833333333333335, 0.35913331696538175, -1.0, 0.0, 0.3569490883855908, -1.0, 0.35991820040899797, 1.0, 1.0, 0.0, 0.35627637130801687, -1.0, 1.0, 0.35326326389325946, -1.0, -1.0, 0.0, 1.0, 0.32558139534883723, 1.0, 1.0, 0.4523809523809524, 0.1144578313253012, 0.37008043665613327, -1.0, 1.0, 0.34850982007965936, 0.07317073170731707, -1.0, -1.0, 0.2717391304347826, 0.36055883933369154, -1.0, 1.0, 0.2236842105263158, 0.24034334763948498, -1.0, 0.0, 1.0, 0.20125786163522014, 1.0, 0.36081959020489757, 0.0, -1.0, 0.34704612894523873, -1.0, -1.0, 0.0, 0.29411764705882354, 0.3325171400587659, -1.0, 0.4032258064516129, -1.0, 1.0, 0.3046875, 0.26666666666666666, 0.3232668848556977, -1.0, -1.0, 0.30434782608695654, 0.2826086956521739, -1.0, 0.3419673603832909, 1.0, 0.4149443561208267, 0.34397366160893217, 0.22448979591836735, 0.3391304347826087, 0.0, 0.34067709480796066, 0.9940828402366864, 0.0, 0.34378273230585066, 0.0, 1.0, 0.36427320490367776, 0.34235631738152483, 1.0, 0.5476190476190477, 0.33079360289680143, 1.0, -1.0, 0.3272889417360285, 0.3669064748201439, 0.3333333333333333, 0.06060606060606061, 0.3249128919860627]
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
