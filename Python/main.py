import AI as ai
import PatternFinder as pf
import numpy as np

model = ai.loadNetwork()
testData = ai.Data()
testData.loadDataFromFile("./data/data-1-100/test1100.txt")

inputs = []
right = 0

def getPredictionFeatures():
    last_three_elements = inputs[-3:]
    fixedList = [0] * (3 - len(last_three_elements)) + last_three_elements
    return np.array(fixedList).reshape(1,-1)

for i in range(len(testData.input)):
    feauters = getPredictionFeatures()
    print(feauters)
    prediction = model.predict(feauters)
    predicted_classes = np.argmax(prediction, axis=1)
    print(f"Input: {testData.input[i]} Guess: {predicted_classes}")
    inputs.append(testData.input[i])
    # print(predicted_classes)
    if (testData.input[i] == predicted_classes):
        right += 1
    # confidence = {index: value for index, value in enumerate(np.array(prediction[0]))}
    # guess = max(confidence, key=confidence.get)
    # print(f"Input: {testData.input[i]} Guess: {guess}")


print(f"Right: {right} Procenteage: {right/len(testData.X)}")


# for i in range(100):
#     data = input()
#     if (data.isnumeric() == False):
#         if (data == 's'):
#             print("stopping")
#             break
#         i-1
#         continue
#     data = int(data)
#     if (0 <= data and data <= 100):

#         prediction = model.predict(getPredictionFeatures())
#         confidence = {index: value for index, value in enumerate(np.array(prediction[0]))}
#         guess = max(confidence, key=confidence.get)
#         print(f"Computer Guessed: {guess}")
#         # print(confidence)
#         inputs.append(data)
        


