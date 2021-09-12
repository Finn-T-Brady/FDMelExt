from MrkvChain_Class import MrkvChain

#functions to be inserted into FoxDot as a Pattern Method
#via >>>Pattern.Markov=Markov
#https://github.com/Qirky/FoxDot/blob/76a4e3ad31a987c6e2c43c38d0440898d3408780/FoxDot/lib/Patterns/Main.py#L1043

def Markov(self,i=None,append=1,Seed=None, Weights=None):
    if(self.data==[]):
        print("Warning: .Markov recieved an empty pattern")
        return self.new([])
    Mrkv=MrkvChain(self.data,Seed,Weights)
    new=[]
    if append==1:
        new=self.data
    if i==None:
        i=len(self.data)
    for x in range(0,i):
        new+=[Mrkv.Next()]
    del Mrkv
    return self.new(new)

#def Cocktail(self,)

def RecursiveIndex(self,i=None,stall=0,start=None):
    if self.data==[]:
        print("Warning: .RecursiveIndex recieved an empty pattern")
        return self.new([])
    new = []
    if stall==0:
        new = RecurStall_0(self.data,i,start)
    if stall==1:
        new = RecurStall_1(self.data,i,start)
    if stall==2:
        new = RecurStall_2(self.data,i,start)
    return self.new(new)

def RecurStall_0(pattern,i=None,start=0):
    new = []
    if i==None:
        i=len(pattern)
    curr=pattern[start]
    new+=[curr]
    for x in range(0,i-1):
        curr=pattern[curr%len(pattern)]
        new+=[curr]
    return new
def RecurStall_1(pattern,i=None,start=None):
    new = []
    if i==None:
        i=len(pattern)
    curr=pattern[start]
    old=-1
    new+=[curr]
    x=0
    for x in range(0,i-1):
        if(curr==old):
            break
        old=curr
        curr=pattern[curr%len(pattern)]
        new+=[curr]
    return new
def RecurStall_2(pattern,i=None,start=None):
    new = []
    if i==None:
        i=len(pattern)
    curr=pattern[start]
    old=-1
    new+=[curr]
    for x in range(0,i-1):
        if(curr!=old):
            curr=pattern[curr%len(pattern)]
        if(curr==old):
            curr=pattern[(curr+1)%len(pattern)]
        new+=[curr]
    return new
