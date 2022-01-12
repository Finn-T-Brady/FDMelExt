from FoxDot import *
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

    def __iter__(self):
        return self.data

TestStr.Markov=Markov

#p=TestStr([0,3,6,9,8,7,6,5,4,3,2,1])
#p=TestStr([])

print("Test1 Starting")
A = [0,3,6,9,8,7,4,1]
p = TestStr(A)
p.Markov(GiveSeed=0)
print("Test1 Passed\n")

print("Test2 Starting")
A = [1,3,5,8,11,3,4,7]

p=TestStr(A)
p.Markov(GiveSeed=0)

assert(list(set(A)) == list(set(p.data)))
print("Test2 Passed\n")


print("Test3 Starting")
A = [2]

p = TestStr(A)
p.Markov(GiveSeed=0)

assert(A==p.data)
print("Test3 Passed\n")

print("Test4 Starting")
A = [1,1,1,1,1,1]

p = TestStr(A)
p.Markov(GiveSeed=0)

assert(A==p.data)
print("Test4 Passed\n")

print("Test5 Starting")
A = [2.4,3.1,6.7]

p = TestStr(A)
p.Markov(GiveSeed=0)
assert(list(set(A)) == list(set(p.data)))
print("Test5 Passed\n")

print("Test6 Starting")
A=[1,3,4,5,7,3,8]

p=TestStr(A)
q=TestStr(A)

p.Markov(Seed=94714)
q.Markov(Seed=94714)
assert(p.data==q.data)
print("Test6 Passed\n")
