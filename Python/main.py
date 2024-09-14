import os
import ML as ml
import Data as data

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

depth = 3
modelName = "model1"
trainFile = "./data/data09/train09.txt"
testFile = "./data/data09/test09.txt"
neuronsmiddle = 18
epoch = 2000




def makeNewNN():
    trainData = data.Data()
    testData = data.Data()
    trainData.loadDataFromFile(trainFile, depth)
    testData.loadDataFromFile(testFile, depth)
    nn = ml.NeuralNetwork()

    nn.ctt(depth, neuronsmiddle, trainData, testData, epoch)
    nn.save(modelName, neuronsmiddle, depth)
    return nn

def loadAndTestOldNetwork():
    nn = ml.NeuralNetwork()
    nn.load(modelName)
    testData = data.Data()
    testData.loadDataFromFile(testFile, depth)
    nn.test(testData)
    return nn

def loadNetwork():
    nn = ml.NeuralNetwork()
    nn.load(modelName)
    return nn


# makeNewNN()
loadAndTestOldNetwork()