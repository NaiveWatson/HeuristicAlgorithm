import numpy as np
import random
import copy
import time
import heapq
import TSP

class FOA():
    def __init__(self,SmellPropability,versionsize,smellsize,codesize):
        self.yourcode=[[]]
        self.BestCode=[]
        self.BestEvaluation=[]
        self.versionsize=versionsize
        self.smellsize=smellsize
        self.codesize=codesize
        self.SmellNum=int(versionsize*SmellPropability)
        self.evaluations=[0 for i in range(versionsize)]

    def Create(self):
        for i in range(self.versionsize):
            self.yourcode[i]=[r for r in range(self.codesize)]
            random.shuffle(self.yourcode[i])



    def Smell(self):
        for i in range(self.versionsize):
            popcentre=self.yourcode[i]
            evaluation=[]
            for v in range(self.smellsize):
                for j in range(self.SmellNum):
                    code[v]=self.Smellmotion(popcentre)
                    while self.Constrain(code)==false:
                        code[v]=self.Smellmotion(popcentre)
                evaluation.append( self.Evaluate(code[v]) )
            self.evaluations[i]=max( evaluation )
            self.yourcode[i]=code[code.index(max(evaluation))]


    def Smellmotion(self,father):
        a=random.randint(0,len(father))
        b=random.randint(0,len(father))
        c=father[a]
        father[a]=father[b]
        father[b]=c
        return father

    def Constration(self,code):
        #if you have constration,add your constration
        return true

    def Evaluate(self,code):
        #write your evaluate function
        evaluation=0
        return evaluation

    def main(self):
        self.Create()
        for i in range(self.generation):
            self.Crossover()
            self.Smell()
            self.BestEvaluation.append(max(self.evaluations))
            maxindex=self.evaluations.index(max(self.evaluations))
            self.BestCode.append(self.yourcode[maxindex])
        besteva=max(self.evaluations)
        bestcode=self.Bestcode[besteva]
        return besteva,bestcode

