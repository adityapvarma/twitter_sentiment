##Generic Graph - Bar

#y=[0,45150,45982,46702,49296,46565,45595,44267,42445,41231,2528]
y=[0,193,219,197,219,199,208,196,191,149,0]
x=[i for i in range(11)]


import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
xnew = np.linspace(min(x), max(x), 300)
plt.rcParams.update({'font.size': 16})

ynew = spline(x, y, xnew)

xlabel=['14:24','14:54','15:24','15:54','16:24','16:54','17:24','17:54','18:24','18:54','19:24']
fig, ax = plt.subplots()
ax.plot(xnew,ynew,'r')
ax.plot(x,y,'ro')
ax.grid(linestyle='--')
plt.xlabel("Time (GMT -1)", labelpad=18)
plt.ylabel("Number of tweets",labelpad=18)
plt.xticks(x,xlabel,rotation=90)

ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

plt.show()
