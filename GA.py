import random
import copy
import time
import heapq
import numpy as np

def create(self,popsize,codesize):
    yourcode=[[]]
    for i in range(popsize):
        yourcode[i]=[r for r in range(codesize)]
        random.shuffle(yourcode[i])
    return yourcode