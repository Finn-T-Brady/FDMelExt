import pickle

from FoxDot import *
from MrkvChainClass import MrkvChain

import os

@PatternMethod
def TrainedMarkov(self,Model=None,length=None,append=1,Seed=None,mloc=(os.environ['APPDATA']+"\\MelExtModels\\")):
    if(Model==None):
        print("No Model Specified")
        return []
    if(self.data==[]):
        print("Warning: .Markov recieved an empty pattern")
        return self.new([])
    Mrkv = MrkvChain([0],Seed=Seed)
    with open(mloc+Model,'rb') as File:
        data=pickle.load(File)
        File.close()
    unique = set(self.data).intersection(set(data.keys()))
    
    for x in unique:
        Mrkv.Nodes[x] = []
        for y in unique:
            Mrkv.Nodes[x] += (data[x][y]//data[x]['gcd']) * [y]
    Mrkv.currVal = list(unique)[0]

    new = []
    if(append==1): new = self.data
    if(length==None): length = len(self.data)
    for x in range(0,length):
        new += [Mrkv.Next()]
    del Mrkv
    return self.new(new)
