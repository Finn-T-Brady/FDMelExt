from MrkvChainClass import MrkvChain
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
#mock Pattern class
class TestStr:
    data = []

    def __init__(self,i):
        self.data=i

    def new(self,i):
        self.data=i

    def __str__(self):
        return self.data.__str__()

TestStr.Markov=Markov

#p=TestStr([0,3,6,9,8,7,6,5,4,3,2,1])
#p=TestStr([])
p=TestStr([0,3,6,9,8,7,4,1])

print(p)

p.Markov()

print(p)
