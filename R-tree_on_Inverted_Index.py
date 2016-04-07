import matplotlib.pyplot as plt
import collections
from data import Test as dict1
from data import Google as dict1
from collections import defaultdict
from collections import OrderedDict
import math
from matplotlib.patches import Rectangle

dict = collections.OrderedDict(sorted(dict1.items()))
x=[]
y=[]
s = dict.keys()
n_occ = {}
def sort_by_n_occurence(dict, N):
    n_occ = {}
    for key in dict.keys():
        try:
            n_occ[dict[key][N-1]]=key
        except:
            continue
    return n_occ         
#first_occ = {dict[key][0]:key for key in dict.keys()}
first_occ = sort_by_n_occurence(dict, 0)
od = collections.OrderedDict(sorted(first_occ.items()))
print od
print j
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
#print IND
    
final=[]
for i in IND:
    tups=[]
    d=1
    while d<=2:
        tups.append(i)
        d=d+1
    final.append(tups)
#print final
import numpy as np
def calc(vals):
    l=len(vals)
    l*=3
    l=int(math.sqrt(l))
    #print l
    j=(len(vals)/l)+1
    buildbuck(l,j,vals)
    
def buildbuck(l,j,vals):
    xrect=[]
    gau=0
    countx=0
    xrect.append([])
    for g,xy in enumerate(vals): # (here is where problem starts)
            if (j!=0):           # there should be xcount divisions
                if(gau < (l-1) ):     #each division should contain xtem rectangles
                    xrect[countx].append(vals[g]) # Need to find a way to append individual rectangles , here all rectangles with same centroid are taken together,mam knows what problem happens here, I've explained her, if doubt ask her.
                    gau=gau+1
                else:
                    xrect[countx].append(vals[g])# Need to find a way to append individual rectangles , here all rectangles with same centroid are taken together 
                    xrect.append([])                    
                    j=j-1
                    countx=countx+1
                    gau=0
    print "\n"     
    print "Printing the sorted y values"
    for i in xrect:
        strbuild(i,1)
        

def pgm(a):
    print "--===========================--"   

    if len(a)>13:
        strbuild(a,0)
    elif len(a)!=0:
        print "This is the final cluster:::: ..", a
 
def strbuild(main,i):
    if i==0:
        print "Printing the sorted x values"
        cents=defaultdict(list)  
        for l in main:
            cents[(l[0][0]+l[1][0])/2.0].append(l)
            OrderedDict(sorted(cents.items(), key=lambda t: t[0]))
        print "C:",cents
        print
        vals=cents.values()
        vals = [val for subl in vals for val in subl] 
        print vals
        calc(vals)
    else:
        #print "\n\nPrinting the sorted y values"
        centy=defaultdict(list)  
        for l in main:
            centy[(l[0][1]+l[1][1])/2].append(l)
            OrderedDict(sorted(centy.items(), key=lambda t: t[0]))
       # print "this is centy  :",centy
        
        valy=centy.values()
        print "----------------------"
        valy = [val for subl in valy for val in subl]# for t in val]    
        
        print valy
        pgm(valy)
print "---==============================================---"
#pgm(final)
xtic = np.unique(np.array(x)).tolist()

plt.plot(x,y,'ro')
plt.xticks(xtic,od.values(),rotation='vertical')
plt.show()

