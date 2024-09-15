import numpy as np



class PatterFinder():
    #Looks if a pattern where a number is contunlsy increasing or decreasing with a given value
    def aritmeticPredictorRaw(self, input, maxStrenght):
        differences = {
            1:0,
            2:0,
            3:0,
            4:0,
            -1:0,
            -2:0,
            -3:0,
            -4:0
        }

        if (len(input) >= maxStrenght):
            for d in differences:
                for i in range(len(input) - 1, len(input) - maxStrenght, -1):
                    newValue = input[i] - d
                    if (newValue == 0): newValue = 9
                    if (newValue == 10): newValue = 1

                    if (newValue == input[i-1]):
                        differences[d] += 1
                    else:
                        break                    

        #Returns a dictionary of each number and how deep it goes untill it finds a new value
        return differences
    
    def aritmeticPredictor(self, input, maxStrenght):
        differences = {
            1:0,
            2:0,
            3:0,
            4:0,
            -1:0,
            -2:0,
            -3:0,
            -4:0
        }

        if (len(input) >= maxStrenght):
            for d in differences:
                for i in range(len(input) - 1, len(input) - maxStrenght, -1):
                    newValue = input[i] - d
                    if (newValue == 0): newValue = 9
                    if (newValue == 10): newValue = 1

                    if (newValue == input[i-1]):
                        differences[d] += 1
                    else:
                        break                    
        
        key = max(differences, key=differences.get)
        value = differences[key]
        return key, value

    def strictPatternPredictorRaw(self, input, depth):
        confidence = {key: 0.0 for key in range(1, 10)}
        for i in range(len(input)):
            retro = i/(len(input))
            for j in range(2, min(depth, len(input) - i)):
                temp, tempc = [], []
                for k in range(j):
                    temp.insert(0, input[i-k])
                    tempc.insert(0, input[-1-k])
                if (temp == tempc): confidence[input[i+1]] += (j-1) * 5 * retro

        # print(confidence)
        return confidence
    
    def strictPatternPredictor(self, input, depth):
        confidence = {key: 0.0 for key in range(1, 10)}
        for i in range(len(input)):
            retro = i/(len(input))
            for j in range(2, min(depth, len(input) - i)):
                temp, tempc = [], []
                for k in range(j):
                    temp.insert(0, input[i-k])
                    tempc.insert(0, input[-1-k])
                if (temp == tempc): confidence[input[i+1]] += (j-1) * 5 * retro

        key = max(confidence, key=confidence.get)
        value = confidence[key]
        return key, value

# temp = [1,3,5,7,9,2,4,6,8]

# pf = PatterFinder()
# pf.aritmeticPredictor(temp, 7)
