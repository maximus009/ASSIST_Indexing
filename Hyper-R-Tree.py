from data import Google
from numpy import unique, array
import matplotlib.pyplot as plt
from collections import OrderedDict

def sort_by_n_occurence(dict, N):
    sortedDict = {}
    for key in dict.keys():
        try:
            sortedDict[dict[key][N-1]]=key
        except:
            continue
    return sortedDict

def plot(x,y, od):
    xtic = unique(array(x)).tolist()
    plt.plot(x,y,'ro')
    plt.xticks(xtic,od.values(),rotation='vertical')
    plt.show()


def something(dict, originalDict):
    od = OrderedDict(sorted(dict.items()))
    print od
    IND,x,y= [],[],[]
    keyWordID = 0
    print od.keys()
    for first_val in od.keys():
        k = od[first_val]
        for i in originalDict[k]:
            IND.append((keyWordID,i))
            x.append(keyWordID)
            y.append(i)
        keyWordID+=1
    plot(x,y,od)
    return IND


def duplicate():
    """
    """
    final=[]
    for i in IND:
        tups=[]
        d=1
        while d<=2:
            tups.append(i)
            d=d+1
        final.append(tups)
    
if __name__=="__main__":
    myDict = Google
    sortedByOccurences = []
    INDS = []
    for n in range(1,10):
        originalDict = OrderedDict(sorted(myDict.items()))
        dict = sort_by_n_occurence(myDict, n)
        sortedByOccurences.append(dict)
        INDS.append(something(dict, originalDict))
