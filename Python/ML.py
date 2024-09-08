import numpy as np
import nnfs
import pickle
from nnfs.datasets import spiral_data

def getData(trainingFile):
    numbers=[]
    X=[]
    y=[]
    f = open(str(trainingFile))

    for line in f:
        

    #For each line
    # for line in f:
    #     elements = line.strip().split()
    #     for number in range(len(line)-5):



    #     # line = line[:-1]
    #     # for number in range(len(line)-3):
    #     #     y.append(int(line[-1]))
    #     #     line = line[:-1]
            
    #     #     tempX = []
    #     #     for i in line[-3:]:
    #     #         tempX.append(int(i))
    #     #     X.append(tempX)
    

    # return np.array(X),np.array(y)
    

def printData(X,y):
    print("Training Data (X):")
    print(np.array(X))  # Prints training features
    print("\nTraining Labels (y):")
    print(np.array(y)) 


np.set_printoptions(threshold=1)
X,y = getData(trainingFile="./Python/datatrain.txt")
printData(X,y)

# class NeuralNetwork():
#     def createNeuralNetwork(self):
