import numpy as np
import random
import copy
import time
import heapq
import os
import math
import json
import FOA
from functools import reduce
from collections import defaultdict


#需求量
require = [ 2 , 1.5 , 4.5 , 3 , 1.5 , 4 , 2.5 , 3 ]

#服务时间
service_time = [ 1 , 2 , 1 , 3 , 2 , 2.5 , 3 , 0.8 ] 

#最早的到达时间
earliest_arrive = [ 1 , 4 , 1 , 4 , 3 , 2 , 5 , 1.5 ]

#最晚的到达时间
latest_arrive = [ 4 , 6 , 2 , 7 , 5.5 , 5 , 8 , 4 ] 

#卸载货物费用
cost = [ 3 , 4 , 5 , 2.5 , 4 , 3 , 5 , 3.5 ] 

#一共有N辆车
N=3

#惩罚权重
W_punish = 10

#货车载重
capacity = 10

SmellPropability = 0.5

versionsize =50

smellsize = 20

codesize =8

def ReadData(file):
    distance = []
    for line in open(file):
        line = line.split(' ')
        distance.append(line)
    return (distance)


def Punishment( star_time , node):
    if star_time < earliest_arrive[node]:
        punish_cost = W_punish * (earliest_arrive[node] - star_time)
    elif star_time > latest_arrive[node]:
        punish_cost = W_punish * (star_time - latest_arrive[node])
    else:
        punish_cost = 0

    return (punish_cost)

def Constraint(code):
    for track in code:
        sum_load = 0
        for node in track:
            sum_load += require[node]
        if sum_load > capacity:
            return False
    return True

def Evaluate(code):
    distance = ReadData(distance_file.txt)
    sum_cost = 0
    for track in code:
        star_time = 0
        for i in range(len(track)+1):
            if i == 0:
                cost_time = distance[0][track[i]] + service_time[track[i]]
                punish_cost = Punishment(star_time , track[i])
                each_cost = cost[track[i]]*require[track[i]]
            elif i == len(track):
                cost_time = distance[track[i]][0] 
            else:
                cost_time = distance[track[i-1]][track[i]] + service_time[track[i]]
                punish_cost = Punishment(star_time , track[i])
                each_cost = cost[track[i]]*require[track[i]]
            star_time = star_time + cost_time
            sum_cost = sum_cost + punish_cost + each_cost


    return (sum_cost)
        



    



if __name__ == "__main__":
    foa = FOA(SmellPropability,versionsize,smellsize,codesize)
    ( Besteva , Bestcode) = foa.main(N)
    print(Besteva)
    print(Bestcode)

