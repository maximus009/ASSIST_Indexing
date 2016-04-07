from rtree import index
from collections import defaultdict
from collections import OrderedDict
from data import Twitter as dict1

dict = OrderedDict(sorted(dict1.items()))
x=[]
y=[]
s = dict.keys()
first_occ = {dict[key][0]:key for key in dict.keys()}

od = OrderedDict(sorted(first_occ.items()))

IND = []
L = 0

for first_val in od.keys():
    k = od[first_val]
    for i in dict[k]:
        IND.append((L,i))
    L+=1

temp=index.Index()
tuples = [(val[0],val[1],val[0],val[1]) for val in IND]

for tup in tuples:
    print tup
    temp.insert(tup[0], tup,obj=42)

print list(temp.nearest((0,20000,0,20000),3, objects = True))
