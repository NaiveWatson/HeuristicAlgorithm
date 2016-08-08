import numpy as np
import random
import copy
import time
import heapq
import TSP

class FOA():
    def __init__(self,MutationPropability,versionsize,smellsize,codesize):
        self.yourcode=[[]]
        self.BestCode=[]
        self.BestEvaluation=[]
        self.versionsize=versionsize
        self.smellsize=smellsize
        self.codesize=codesize
        self.MutationPropability=MutationPropability
        self.evaluations=[0 for i in range(versionsize)]

    def Create(self):
        for i in range(self.versionsize):
            self.yourcode[i]=[r for r in range(self.codesize)]
            random.shuffle(self.yourcode[i])

    def Crossmotion(self,fater,mother):
        a=random.randint(0,len(father)/2-1)
        b=random.randint(len(father)/2,len(mother)-1)
        s=father[0:a]+mother[a:b]+father[b:]
        son=[]
        for i in s:
            if i not in son:
                son.append(i)
        return son

    def Mutation(self):
        for i in range(len(self.yourcode)):
            if random.uniform(0,1)<self.MutationPropability:
                code=self.Mutationmotion(self.yourcode[i])
                while self.Constrain(code)==false:
                    code=self.Crossmotion(self.yourcode[i],self.yourcode[random.randint(0,len(self.yourcode))])
                self.yourcode[i]=code
                
    def Crossover(self):
        code=[[0 for i in range(len(self.yourcode[0]))] for j in range(len(self.yourcode))]
        for i in range(len(self.yourcode)):
            code[i]=self.Crossmotion(self.yourcode[i],self.yourcode[random.randint(0,len(self.yourcode))])
            while self.Constrain(code[i])==false:
                code[i]=self.Crossmotion(self.yourcode[i],self.yourcode[random.randint(0,len(self.yourcode))])
        selectpropability=self.Selectpropability(code)
        for j in range(len(code)):
            if random.uniform(0,1)<selectpropability[j]:
                self.yourcode[j]=code[j]

    def Mutationmotion(self,father):
        a=random.randint(0,len(father))
        b=random.randint(0,len(father))
        c=father[a]
        father[a]=father[b]
        father[b]=c
        return father

    def Constration(self,code):
        #if you have constration,add your constration
        return true

    def Evaluate(self,codes):
        #write your evaluate function
        evaluation=0
        return evaluation

    def SelectPropability(self,code):
        self.evaluations=self.Evaluate(code)
        selectpropability=[self.evaluations[i]/sum(self.evaluations) for i in range(len(self.evaluations))]
        return selectpropability

    def main(self):
        self.Create()
        for i in range(self.generation):
            self.Crossover()
            self.Mutation()
            self.BestEvaluation.append(max(self.evaluations))
            maxindex=self.evaluations.index(max(self.evaluations))
            self.BestCode.append(self.yourcode[maxindex])
        besteva=max(self.evaluations)
        bestcode=self.Bestcode[besteva]
        return besteva,bestcode

