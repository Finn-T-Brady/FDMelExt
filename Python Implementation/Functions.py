from MrkvChain_Class import MrkvChain

#functions to be inserted into FoxDot as a Pattern Method
#via the @PatternMethod function decorator

@PatternMethod
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

@PatternMethod
def Cocktail(self,append=1,i=None,step=0, d=0,dbg=False):
    if self.data==[]:
        print("Warning: .Cocktail recieved an empty pattern")
        return self.new([])
    if(i==None):
        i=len(self.data)
        i=i*i
    new=[]
    if(append==1):
        new=self.data
    new+=[CTailFwdStp,CTailFwdPass,CTailBkwdStp,CTailBkwdPass][2*d+step](self.data,i)
    if(dbg):
        print(new)
    return self.new(new)

def CTailFwdStp(data,i):
    new=[]
    swapped = True
    start=0
    end = len(data)-1
    while (swapped and i>=0):
        for i in range(start, end):
            if(data[i]>data[i+1]):
                data[i], data[i+1] = data[i+1],data[i]
                swapped = True
            new+=data
        if(swapped == False):
            break
        end = end - 1
        for i in range(end-1,start-1,-1):
            if(data[i] > data[i+1]):
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
            new+=data
        start = start +1
        i-=1
    return new
def CTailFwdPass(data,i):
    new=[]
    swapped = True
    start=0
    end = len(data)-1
    while (swapped and i>=0):
        for i in range(start, end):
            if(data[i]>data[i+1]):
                data[i], data[i+1] = data[i+1],data[i]
                swapped = True
        if(swapped == False):
            break
        end = end - 1
        for i in range(end-1,start-1,-1):
            if(data[i] > data[i+1]):
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
        start = start +1
        new+=data
        i-=1
    return new
def CTailBkwdStp(data,i):
    new=[]
    swapped = True
    start=0
    end = len(data)-1
    while (swapped and i>=0):
        for i in range(end-1,start-1,-1):
            if(data[i] > data[i+1]):
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
            new+=data
        if(swapped == False):
            break
        start = start +1
        for i in range(start, end):
            if(data[i]>data[i+1]):
                data[i], data[i+1] = data[i+1],data[i]
                swapped = True
            new+=data
        end = end - 1
        i-=1
    return new
def CTailBkwdPass(data,i):
    new=[]
    swapped = True
    start=0
    end = len(data)-1
    while (swapped and i>=0):
        for i in range(end-1,start-1,-1):
            if(data[i] > data[i+1]):
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
        if(swapped == False):
            break
        start = start +1
        for i in range(start, end):
            if(data[i]>data[i+1]):
                data[i], data[i+1] = data[i+1],data[i]
                swapped = True
        end = end - 1
        new+=data
        i-=1
    return new

@PatternMethod
def RecursiveIndex(self,append=1, i=None,stall=0,start=0):
    if self.data==[]:
        print("Warning: .RecursiveIndex recieved an empty pattern")
        return self.new([])
    if i==None:
        i=len(self.data)
    new = []
    if stall==0:
        new = RecurStall_0(self.data,i,start)
    if stall==1:
        new = RecurStall_1(self.data,i,start)
    if stall==2:
        new = RecurStall_2(self.data,i,start)
    if(append==1):
        new=self.data+new
    return self.new(new)

def RecurStall_0(pattern,i=None,start=0):
    new = []
    curr=pattern[start]
    new+=[curr]
    for x in range(0,i-1):
        curr=pattern[curr%len(pattern)]
        new+=[curr]
    return new
def RecurStall_1(pattern,i=None,start=0):
    new = []
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
def RecurStall_2(pattern,i=None,start=0):
    new = []
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
