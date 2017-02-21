import numpy as np
import random
import copy
import time
import heapq
import VRP

class FOA():
    def __init__(self,SmellPropability,versionsize,smellsize,codesize):
        self.yourcode=[]
        self.BestCode=[]
        self.BestEvaluation=[]
        self.versionsize=versionsize
        self.smellsize=smellsize
        self.codesize=codesize
        self.SmellNum=int(versionsize*SmellPropability)
        self.evaluations=[0 for i in range(versionsize)]

    def Create(self , N):
        for i in range(self.versionsize):
            code_cut=[]
            code=[r for r in range(self.codesize)]
            random.shuffle(code)
            for i in range(N):
                a = i+1
                if a < N:
                    code_cut.append(code[i*N:a*N])
            self.yourcode.append(code_cut)
                



    def Smell(self , N):
        for i in range(self.versionsize):
            popcentre=self.yourcode[i]
            evaluation=[]
            code = [0 for i in range(self.smellsize)]
            for v in range(self.smellsize):
                for j in range(self.SmellNum):
                    code[v]=self.Smellmotion(popcentre , N)
                    while self.Constraint(code)==false:
                        code[v]=self.Smellmotion(popcentre)
                evaluation.append( self.Evaluate(code[v]) )
            self.evaluations[i]=max( evaluation )
            self.yourcode[i]=code[code.index(max(evaluation))]


    def Smellmotion(self , father , N):
        Na = random.randint(0,N)
        Nb = random.randint(0,N)
        a=random.randint(0,len(father[Na]))
        b=random.randint(0,len(father[Nb]))
 
        (father[Na][a],father[Nb][b]) = (father[Nb][b],father[Na][a])

        return father

    def Constraint(self,code):
        judge = VRP.Constraint(code)
        return judge

    def Evaluate(self,code):

        evaluation= VRP.Evaluate(code)
        return evaluation

    def main(self , N):
        self.Create(N)
        for i in range(self.generation):
            self.Crossover()
            self.Smell()
            self.BestEvaluation.append(max(self.evaluations))
            maxindex=self.evaluations.index(max(self.evaluations))
            self.BestCode.append(self.yourcode[maxindex])
        besteva=max(self.evaluations)
        bestcode=self.Bestcode[besteva]
        return besteva,bestcode

