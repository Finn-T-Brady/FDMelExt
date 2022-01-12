#Libraries to randomly seed Markov Chain class
from random import Random
from time import time_ns as timeStamp


class MrkvChain:
    #Nodes are formated as {nodeValue:[links, numbers are repeated to add weight]} e.g.{4:[1,3,3,5,2]}
    Nodes = {}

    #The crrent node selected by the chain
    currVal = None

    #Preparing the Random Class
    rng = Random(None)

    #weights for value n infront, formatted [n, weight]
    dWeights = [[1,4],[2,2],[3,1],[-1,1]]

    #the Next() Method returns the current value and selects the next value for the chain
    def Next(self):
        val=self.currVal
        links=self.Nodes[val]
        self.currVal=links[self.rng.randint(0,len(links)-1)]
        return val

    #the ArrayDecomp() method takes an array, loops through it, and for each note calculates the probalities for the next possible nots
    def ArrayDecomp(self,Arr):
        t=len(Arr)
        #initialising dict
        for x in Arr:
            self.Nodes[x]=[]
        #adding notes to arrays
        for x in range(0,t):
            for n in self.dWeights:
                self.Nodes[Arr[x]]+=n[1]*[Arr[(x+n[0])%t]]

    #the Initialisation function which is calles
    def __init__(self,Arr=None,Seed=None,Weights=None):
        #if a seed is not given
        if Seed==None:
            #checks the timestamp and modulos if by 0xFFFFFFFF (2^24-1)
            tempSeed=timeStamp()%0xFFFFFFFF
            #Printing seed in hex so it can be reused if it sounded good, it is in hex to make it more readable
            print("MrkvChain seed:"+hex(tempSeed))
            #initialising the random class
            self.rng.seed(tempSeed)

        #initialises the random class if a seed is provided
        if Seed!=None:
            self.rng.seed(Seed)
        #replaces the default dWeights values
        if Weights!=None:
            self.dWeights=Weights
        #if an array is provided it will decompose it to the probabilities
        if Arr!=None:
            self.ArrayDecomp(Arr)
            self.currVal=Arr[0]
