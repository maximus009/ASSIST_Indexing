import matplotlib.pyplot as plt
import collections
from data import Google as dict1

print dict1

dict = collections.OrderedDict(sorted(dict1.items()))
x=[]
y=[]
s = dict.keys()
first_occ = {dict[key][0]:key for key in dict.keys()}
print first_occ.keys()

od = collections.OrderedDict(sorted(first_occ.items()))
print od.keys()
    
IND = []
L = 0

for first_val in od.keys():
    k = od[first_val]
    for i in dict[k]:
        IND.append((L,i))
    L+=1

for i in IND:
    x.append(i[0])
    y.append(i[1])
print IND
import numpy as np

xtic = np.unique(np.array(x)).tolist()

plt.plot(x,y,'ro')
plt.xticks(xtic,od.values(),rotation='vertical')
plt.show()

