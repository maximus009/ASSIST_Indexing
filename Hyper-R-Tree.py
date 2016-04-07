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

fileChar = 1
def plot(x,y, od):
    global fileChar
    f = plt.figure()
    xtic = unique(array(x)).tolist()
    plt.plot(x,y,'bo')
    plt.xticks(xtic,od.values(),rotation='vertical')
    plt.savefig(str(fileChar)+'.png')
    fileChar+=1
    plt.show()

def create_plot_data(dict, originalDict):
    od = OrderedDict(sorted(dict.items()))
    IND,x,y= [],[],[]
    keyWordID = 0
    keyMap = {}
    for first_val in od.keys():
        k = od[first_val]
        keyMap[keyWordID]=k
        for i in originalDict[k]:
            IND.append((keyWordID,i))
            x.append(keyWordID)
            y.append(i)
        keyWordID+=1
#    plot(x,y,od)
    return IND,keyMap


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
    
def main():
    myDict = Google
    sortedByOccurences = []
    INDS = []
    maxOccurences = max([len(myDict[key]) for key in myDict])
    keyMaps = []
    for n in range(1,5):
        originalDict = OrderedDict(sorted(myDict.items()))
        dict = sort_by_n_occurence(myDict, n)
        sortedByOccurences.append(dict)
        plotData,keyMap = create_plot_data(dict,originalDict)
        INDS.append(plotData)
        keyMaps.append(keyMap)
        break
    print keyMaps
    for i in INDS:
        print i

main()
