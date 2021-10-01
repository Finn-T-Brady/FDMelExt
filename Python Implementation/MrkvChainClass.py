import random
from time import time_ns as timeStamp
class MrkvChain:
    #Nodes are formated as {nodeValue:[links, numbers are repeated to add weight]} e.g.{4:[1,3,3,5,2]}
    Nodes = {}
    currVal = None

    rng = random.Random(None)

    dWeights = [[1,4],[2,2],[3,1],[-1,1]]#weights for value n infront, formatted [n, weight]

    def Next(self):
        val=self.currVal
        links=self.Nodes[val]
        self.currVal=links[self.rng.randint(0,len(links)-1)]
        return val
    
    def ArrayDecomp(self,Arr):
        t=len(Arr)
        for x in Arr:
            self.Nodes[x]=[]
        for x in range(0,t):
            for n in self.dWeights:
                self.Nodes[Arr[x]]+=n[1]*[Arr[(x+n[0])%t]]
    
    def __init__(self,Arr=None,Seed=None,Weights=None):
        if Seed==None:
            tempSeed=timeStamp()%0xFFFFFFFF
            print("MrkvChain seed:"+hex(tempSeed))
            self.rng.seed(tempSeed)
        if Seed!=None:
            self.rng.seed(Seed)
        if Weights!=None:
            self.dWeights=Weights
        if Arr!=None:
            self.ArrayDecomp(Arr)
            self.currVal=Arr[0]
            self.Next()
