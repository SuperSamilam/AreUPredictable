

#This script is used to find sctrict patterns in the input



class FindStrictPatternsAI():
    def FindRepetingPattern(self, data):
        #Look -10 of the input dataset to try and find patterns
        confidence = {i: 0 for i in range(101)}

        for i in range(len(data.input)):
            confidence = {i: 0 for i in range(101)}
            retro = i / (len(data.input))
            confidence[data.input[i]] += 0.7 * retro
            for j in range(2, min(100, len(data.input) - i)):
                temp, tempc = [], []
                for k in range(j):
                    temp.insert(0, data.input[i-k])
                    tempc.insert(0, data.input[-1-k])
                if temp == tempc: confidence[data.input[i+1]] += (j-1) * 10.9 * retro
                else: break
        
        print(confidence)