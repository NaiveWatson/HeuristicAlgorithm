#import numpy as np
import random
import copy
import time
import heapq
import os
import math
import json
from functools import reduce
from collections import defaultdict

TSPdata=defaultdict(list)

def ReadData(file):

    f=open("data/"+file)
    Data=f.readlines()
    information=Data[0:7]
    print ( "data information" )
    for i in range(len(information)):
        print ( information[i] )
    for da in Data[7:]:
        li=[]
        if da == 'EOF\n':
            break
        else:
            d=da.split(' ')
            for j in d:
                if j!= '':
                    li.append(json.loads(j))
            TSPdata[li[0]].append(li[1])
            TSPdata[li[0]].append(li[2])
    f.close()

def Evaluate(code):
    DistanceList=list(map(lambda i: math.sqrt((TSPdata[code[i]][0]-TSPdata[code[i-1]][0])**2+(TSPdata[code[i]][1]-TSPdata[code[i-1]][1])**2),range(1,len(code))))
    distance=reduce(lambda x,y: x+y , DistanceList)
    return distance
        



    



if __name__ == "__main__":
    p=os.getcwd()
    path=p+"/data"
    allfiles=os.listdir(path)
    for file in allfiles:
        ReadData(file)
        #code=[x+1 for x in range(len(TSPdata))]
        #Evaluate(code)

