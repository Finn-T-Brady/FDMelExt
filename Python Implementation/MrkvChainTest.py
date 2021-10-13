from Functions import Markov

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
