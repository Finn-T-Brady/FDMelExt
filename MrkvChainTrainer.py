from sys import argv
import pickle

fileName="TrainingData/"+argv[1]
FileOpen = file.open(fileName,'r')
UData = pickle.Unpickler(FileOpen)
