from MrkvChain_Class import MrkvChain

#function to be inserted into FoxDot as a Pattern Method
def Markov(self,i=None,append=1,Seed=None, Weights=None):
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
