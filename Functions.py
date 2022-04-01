from FoxDot import *
from MrkvChainClass import MrkvChain
from TrainedMarkov import TrainedMarkov

#functions to be inserted into FoxDot as a Pattern Method
#via the @PatternMethod function decorator

#This is the function to decompose a FoxDot Pattern into a Markov Chain and them recompose a pattern
@PatternMethod
def Markov(self,Length=None,append=1,Seed=None, Weights=None,debug=0):
    #check for empty pattern
    if(self.data==[]):
        print("Warning: .Markov recieved an empty pattern")
        return self.new([])
    #initialises markov chain with given pattern, seed, and weights
    Mrkv=MrkvChain(self.data,Seed,Weights)
    new=[]
    #if no lenght is given, takes length of given data
    if Length==None:
        Length=len(self.data)
    #gets new value from markov chain class for specified length
    for x in range(0,Length):
        new+=[Mrkv.Next()]
    del Mrkv
    #debug argument at request of client
    if debug==1:
        print(new)
    #if the append argument is set to 1 it appends the generate pattern to the end of the original one
    if append==1:
        new=self.data+new
    return self.new(new)

@PatternMethod
def Cocktail(self,append=1,Length=None,step=0, Backwards=0,debug=False):
    #check for empty pattern
    if self.data==[]:
        print("Warning: .Cocktail recieved an empty pattern")
        return self.new([])
    #if no length given it takes the square of 
    if(Length==None):
        Length=len(self.data)
        if(step==1):
            Length=Length*Length
    new=[]
    if(append==1):
        new=self.data
    #selecting from an array of functions instead of using if statements
    new+=[CTailFwdStp,CTailFwdPass,CTailBkwdStp,CTailBkwdPass][2*Backwards+step](self.data,Length)
    if(debug):
        print(new)
    return self.new(new)

#The function for cocktail in step mode moving forwards first
def CTailFwdStp(data,i):
    new=[]
    swapped = True
    start=0
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
#The function for cocktail in pass mode moving forwards first
def CTailFwdPass(data,i):
    new=[]
    swapped = True
    start=0
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
#The function for cocktail in step mode moving backwards first
def CTailBkwdStp(data,i):
    new=[]
    swapped = True
    start=0
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
#The function for cocktail in pass mode moving backwards first
def CTailBkwdPass(data,i):
    new=[]
    swapped = True
    start=0
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

#The 
@PatternMethod
def RecursiveIndex(self,append=1, Length=None,stall=2,start=0, debug=0):
    if self.data==[]:
        print("Warning: .RecursiveIndex recieved an empty pattern")
        return self.new([])
    if Length==None:
        Length=len(self.data)
    new = []
    new = [RecurStall_0,RecurStall_1,RecurStall_2][stall](self.data,Length,start)
    if debug==1:
        print(new)
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
        old=curr
    return new
