import numpy as np

class Data():
    def loadDataFromFile(self, filename, depth):
        self.X = []
        self.y = []
        self.input = []

        with open(filename, 'r') as file:
            self.data = file.read()

        self.data = [int(num.strip()) for num in self.data.split(',') if num.strip()]
        self.input = np.array(self.data)
        self.setupData(depth)

    def makeRandomDataSet(self, depth):
        self.X = []
        self.y = []
        self.data = ""
        self.input = []

        for i in range(100):
            self.data += str(np.random.randint(0, 10)) + ", "
        self.data = [int(num.strip()) for num in self.data.split(',') if num.strip()]
        self.input = self.data
        self.setupData(depth)
        
    def setupData(self, depth):
        i = depth + 1
        while i < len(self.data):
            label = int(self.data[i])
            j = i - depth
            features = list(self.data[j:j+3])
            features = [int(x) for x in features]
            self.X.append(features)
            self.y.append(label)
            i += 1

        self.X = np.array(self.X)
        self.y = np.array(self.y)

