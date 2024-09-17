import numpy as np
import os
import ML as ml
import PatternFinder as pf
import Data as data

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

modelName = "model-2"
trainFile = "./data/data09/train09.txt"
testFile = "./data/data09/test09.txt"
neuronsmiddle = 18
epoch = 2000

depth = 3
atrimeticDepth = 5
strictDepth = 15



#AI
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

#Helpers
def get_last_three_elements(list):
    if len(list) < 3:
        return [0] * (3 - len(list)) + list
    else:
        return list[-3:]

def initalizeNewGame():
    patternFinder = pf.PatterFinder()
    nn = loadNetwork()
    return patternFinder, nn

def humanPlay():
    patternFinder, nn = initalizeNewGame()
    inputed = []
    right = 0.0

    while (True):
        input = input()
        if (data.isnumeric() == False):
            if (data == 's'):
                    print("stopping")
            break
            i-1
            continue
        data = int(data)
        if (0 <= data and data <= 9):
            inputs = np.array(get_last_three_elements(inputed)).reshape(1, -1)
            aiConfidence = nn.predictRaw(inputs)
            depthNumber, patternDepth = patternFinder.aritmeticPredictor(inputed, atrimeticDepth)
            number, numberConfidence = patternFinder.strictPatternPredictor(inputed, strictDepth)

            guess = np.argmax(aiConfidence)
            if (numberConfidence > 1.5):#confidence is very high meaning it probely is a pattern
                guess = number
            elif (patternDepth >= 3): #3 numbers has been incresing contunisly in a direction example 1,2,3
                guess = depthNumber
            elif (i == 0):
                guess = 7

            if (data == guess):
                right = right + 1
            
            inputed.append(data)

        accuracy = right/len(inputed)
        print(f"Accuracy: {accuracy}")


def autoPlay():
    patternFinder, nn = initalizeNewGame()
    testData = data.Data()
    testData.loadDataFromFile(testFile, depth)
    inputed = []

    right = 0.0

    for i in range(len(testData.input)):
        #Get 3 input numbers
        inputs = np.array(get_last_three_elements(inputed)).reshape(1, -1)
        aiConfidence = nn.predictRaw(inputs)
        depthNumber, patternDepth = patternFinder.aritmeticPredictor(inputed, atrimeticDepth)
        number, numberConfidence = patternFinder.strictPatternPredictor(inputed, strictDepth)

        guess = np.argmax(aiConfidence)
        if (numberConfidence > 1.5):#confidence is very high meaning it probely is a pattern
            guess = number
        elif (patternDepth >= 3): #3 numbers has been incresing contunisly in a direction example 1,2,3
            guess = depthNumber
        elif (i == 0):
            guess = 7

        if (testData.input[i] == guess):
            right = right + 1

        inputed.append(testData.input[i])

    accuracy = right/len(testData.input)
    print(f"Accuracy: {accuracy}")


# autoPlay()
# makeNewNN()
# nn = loadNetwork()
# print(nn.model)
# tfjs.converters.save_keras_model(nn.model, "webmodel")