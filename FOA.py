import numpy as np
import random
import copy
import time
import heapq
import VRP

class FOA(object):
    def __init__(self,SmellPropability,versionsize,smellsize,codesize,generation):
        self.yourcode=[]
        self.BestEvaluation=[]
        self.versionsize=versionsize
        self.smellsize=smellsize
        self.codesize=codesize
        self.generation = generation
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
                else:
                    code_cut.append(code[i*N:])
            self.yourcode.append(code_cut)
                



    def Smell(self , N):
        for i in range(self.versionsize):
            popcentre=self.yourcode[i]
            evaluation=[]
            code = []
            for v in range(self.smellsize):
                for j in range(self.SmellNum):
                    aaa=self.Smellmotion(popcentre , N)
                    while self.Constraint(aaa)==False:
                        aaa=self.Smellmotion(popcentre , N)
                code.append(copy.deepcopy(aaa))
                evaluation.append( self.Evaluate(aaa) )
            self.evaluations[i]=min( evaluation )
            self.yourcode[i]=code[evaluation.index(min(evaluation))]


    def Smellmotion(self , father , N):
        Na = random.randint(0,N-1)
        Nb = random.randint(0,N-1)
        a=random.randint(0,len(father[Na])-1)
        b=random.randint(0,len(father[Nb])-1)
        c=father[Na][a]
        father[Na][a]=father[Nb][b]
        father[Nb][b]=c


        return father

    def Constraint(self,code):
        judge = VRP.Constraint(code)
        return judge

    def Evaluate(self,code):

        evaluation= VRP.Evaluate(code)
        return evaluation

    def main(self , N):
        BestCode=[]
        self.Create(N)
        for i in range(self.generation):
            #self.Crossover()
            self.Smell(N)
            self.BestEvaluation.append(min(self.evaluations))
            #print (min(self.evaluations)/len(self.evaluations))
            minindex=self.evaluations.index(min(self.evaluations))
            aaa=self.yourcode[minindex]
            BestCode.append(copy.deepcopy(aaa))
        besteva=min(self.BestEvaluation)
        avergeeva = sum(self.BestEvaluation)/len(self.BestEvaluation)
        minindex=self.BestEvaluation.index(besteva)
        bestcode=BestCode[minindex]
        return (besteva,bestcode,avergeeva,self.BestEvaluation)

