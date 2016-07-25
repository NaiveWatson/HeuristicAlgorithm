import numpy as np
import random
import copy
import time
import heapq
import os
import json
from collections import defaultdict

TSPdata=defaultdict(list)

def ReadData(file):

    f=open("data/"+file)
    Data=f.readlines()
    information=Data[0:7]
    print "data information"
    for i in range(len(information)):
        print information[i]
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


        



    



if __name__ == "__main__":
    p=os.getcwd()
    path=p+"/data"
    allfiles=os.listdir(path)
    for file in allfiles:
        ReadData(file)

