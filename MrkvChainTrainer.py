import argparse
import pickle
import os

parser = argparse.ArgumentParser(description="Pain.")
parser.add_argument('--file',help='file to train model off',type=str)
parser.add_argument('--model',help='The model that will be trained',type=str)
parser.add_argument('--mloc',help='the location of the named model',type=str,default=os.environ['APPDATA']+"\\MelExtModels")
parser.add_argument('--rec',help='for if the pickled data being read is broken into chunks',type=bool,default=False)
parser.add_argument('--weights',help='the weights for the odds of a number moving to a given relative position',default=[[1,4],[2,2],[3,1],[-1,1]],nargs='+')
parser.add_argument('--floc',help="training data directory",type=str,default='TrainingData')
parser.add_argument('--MDE',help="Enables manual data entry",type=bool,default=False)
parser.add_argument('--D',help="Manually entered data",nargs='+')
args=parser.parse_args()

#function to calculate the gcd of two numbers
def gcd(a,b):
    while b:
        a,b=b,b%a
    return a

#function to estimate the greatest common divisor of a list of numbers
def lGcd(List):
    n1 = List[0]
    n2 = List[1]
    currGcd = gcd(n1,n2)

    for i in range(2,len(List)):
        currGcd = gcd(currGcd,List[i])
    
    return currGcd


readData = []
with open(args.floc+'\\'+args.file,'rb') as FileOpen:
    UData = pickle.load(FileOpen)
    if(not args.rec):
        readData = UData["degree"]
    else:
        for x in UData["degree"]:
            readData+=x
    FileOpen.close()

#data from Training will be stored in the format of [[GCD of 0,P(0 to 0),P(0 to 1),...,P(0 to n)],[GCD of 1,P(1 to 0),...,P(1 to n)],[GCD of n,P(n to 0),...,P(n to n)]
modelData = {}
modelNew = not os.path.exists(args.mloc+"\\"+args.model)
if(modelNew):
    for x in list(set(readData)):
        modelData[x] = {}
        for y in list(set(readData)):
            modelData[x][y] = 0
else:
    with open(args.mloc+"\\"+args.model,'rb') as FileOpen:
        modelData = pickle.load(FileOpen)
        FileOpen.close()
        newVals = list(set(readData)-set(modelData.keys()))
        oldVals = list(modelData.keys())
        for x in newVals:
            modelData[x]={}
        for x in newVals:
            for y in list(modelData.keys()):
                modelData[x][y]=0
        for x in oldVals:
            for y in newVals:
                modelData[x][y]=0

for i in range(0,len(readData)):
    for j in args.weights:
        modelData[readData[i]][readData[(i+j[0])%len(readData)]]+=j[1]

for x in list(modelData.keys()):
    listToFactor=[]
    for i in list(modelData[x].keys()):
        if(i!='gcd' and modelData[x][i]!=0):
            listToFactor+=[modelData[x][i]]
    g = lGcd(listToFactor)
    modelData[x]['gcd']=g

if(not os.path.exists(args.mloc)):
    os.mkdir(args.mloc)

with open(args.mloc+"\\"+args.model,'wb') as FileOpen:
    pickle.dump(modelData,FileOpen)
    FileOpen.close()
