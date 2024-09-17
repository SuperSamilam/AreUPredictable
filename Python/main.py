import numpy as np
import os
import ML as ml
import PatternFinder as pf
import Data as data

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

modelName = "model-2"
trainFile = "./data/data09/train09.txt"
testFile = "./data/data09/testAuto.txt"
neuronsmiddle = 18
epoch = 2000

depth = 3
atrimeticDepth = 4
strictDepth = 100



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

    keyAmounts = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0,
    }

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

            sum = 0.0
            for value in keyAmounts.values():
                sum += value
            
            for key in keyAmounts.keys():
                aiConfidence[0][key] += keyAmounts[key]/(max(sum*2, 1))

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
            keyAmounts[data] += 1

        accuracy = right/len(inputed)
        print(f"Accuracy: {accuracy}")


def autoPlay():
    patternFinder, nn = initalizeNewGame()
    testData = data.Data()
    testData.loadDataFromFile(testFile, depth)
    inputed = []

    right = 0.0

    keyAmounts = {
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            9:0
        }
    aiRight = {
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            9:0
        }

    for i in range(len(testData.input)):
        #Get 3 input numbers
        inputs = np.array(get_last_three_elements(inputed)).reshape(1, -1)
        aiConfidence = nn.predictRaw(inputs)
        depthNumber, patternDepth = patternFinder.aritmeticPredictor(inputed, atrimeticDepth)
        number, numberConfidence = patternFinder.strictPatternPredictor(inputed, strictDepth)
        

        sum = 0
        for value in keyAmounts.values():
            sum += value
            
        for key in keyAmounts.keys():
            aiConfidence[0][key] += keyAmounts[key]/(max(sum, 1))*2

        guess = np.argmax(aiConfidence)
        if (numberConfidence > 1):#confidence is very high meaning it probely is a pattern
            guess = number
        elif (patternDepth >= 3): #3 numbers has been incresing contunisly in a direction example 1,2,3
            guess = depthNumber
        elif (i == 0):
            guess = 7

        keyAmounts[testData.input[i]] += 1
        if (testData.input[i] == guess):
            right = right + 1
            aiRight[testData.input[i]] += 1

        inputed.append(testData.input[i])

    accuracy = right/len(testData.input)
    print(f"Accuracy: {accuracy}")
    print(f"Amount of times pressed each key: {keyAmounts}")
    print(f"What numbers did the AI guess right: {aiRight}")


# autoPlay()
# makeNewNN()
nn = loadNetwork()
autoPlay()
# loadAndTestOldNetwork()
# print(nn.model)
# tfjs.converters.save_keras_model(nn.model, "webmodel")