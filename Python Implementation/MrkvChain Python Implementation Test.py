from MelExtPyTest import MrkvChain

test1 = MrkvChain([1,1,4,4,7,7,6,5,4,3,2,1])
print(test1.Nodes)
for a in range(0,8):
    test1 = MrkvChain([1,1,4,4,7,7,6,5,4,3,2,1])
    a1= []
    for x in range(0,32):
        a1+=[test1.Next()]
    print(a1)

