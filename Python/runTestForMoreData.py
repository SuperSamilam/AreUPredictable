import numpy as np
import os
import ML as ml
import PatternFinder as pf
import Data as data
import main as m

modelName = "model-2"
trainFile = "./data/data09/train09.txt"
testFile = "./data/data09/testAuto.txt"

depth = 3
atrimeticDepth = 4
strictDepth = 100

def loadNetwork():
    nn = ml.NeuralNetwork()
    nn.load(modelName)
    return nn

def initalizeNewGame():
    patternFinder = pf.PatterFinder()
    nn = loadNetwork()
    return patternFinder, nn

playerKeyPressedAmounts = {
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

AiGuessesAmount = {
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

AIRightGuessesAmount = {
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

patternFinder, nn = initalizeNewGame()

testData = data.Data()
testData.loadDataFromFile(testFile, depth)
inputed = []
aiGuesses = []

right = 0.0
for i in range(len(testData.input)):
    inputs = np.array(m.get_last_three_elements(inputed)).reshape(1, -1)
    aiConfidence = nn.predictRaw(inputs)
    depthNumber, patternDepth = patternFinder.aritmeticPredictor(inputed, 4)
    number, numberConfidence = patternFinder.strictPatternPredictor(inputed, 15)

    guess = np.argmax(aiConfidence)
    if (numberConfidence > 1.5):#confidence is very high meaning it probely is a pattern
        guess = number
    elif (patternDepth >= 3): #3 numbers has been incresing contunisly in a direction example 1,2,3
        guess = depthNumber
    elif (len(inputed) == 0):
        guess = 7

    if (testData.input[i]  == guess):
        right = right + 1
        AIRightGuessesAmount[testData.input[i]] += 1
    
    playerKeyPressedAmounts[testData.input[i]] += 1
    AiGuessesAmount[guess] += 1
    inputed.append(testData.input[i])
    aiGuesses.append(guess)
        
print(f"Amount of numbers gussed right: {right}")
print(f"Accuracy: {right/len(inputed)}")
print(f"How many times the key got pressed by player: {playerKeyPressedAmounts}")
print(f"How many times the AI guessed each number: {playerKeyPressedAmounts}")
print(f"How many times the AI guessed right of each number: {AIRightGuessesAmount}")
print(f"AI Guesses: {aiGuesses}")