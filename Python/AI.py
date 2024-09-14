import tensorflow as tf
from tensorflow import keras
import numpy as np
import PatternFinder as pattern

modelName = "0-100model2"

class Data():
    def loadDataFromFile(self, filename, depth = 3):
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

class NeuralNetwork():
    def load(self):
        self.model = tf.keras.models.load_model("./models/" + modelName + '.keras')

    def create(self):
        self.model = tf.keras.Sequential()
        self.model.add(tf.keras.layers.Dense(units=50, input_dim=3))
        self.model.add(tf.keras.layers.Dense(units=170, activation='relu'))
        self.model.add(tf.keras.layers.Dense(units=101))

        opt = keras.optimizers.Adam(learning_rate=0.05)

        self.model.compile(optimizer='adam',
                    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                    metrics=['accuracy'])
    
    def train(self, data):
       self. model.fit(data.X, data.y, epochs=800)

    def test(self, data):
        loss, accuracy = self.model.evaluate(data.X,  data.y, verbose=2)
        # print(f"Loss: {loss} Accuracy: {accuracy}")

    def save(self):
        self.model.save("./models/" + modelName + '.keras')

    def predict(self, inputdata):
        prediction = self.model.predict(inputdata)
        return prediction

    def runRandomTests(self, amount, depth):
        meanAccuracy = []
        for i in range(amount):
            data = Data()
            data.makeRandomDataSet(depth)
            loss, accuracy = self.model.evaluate(data.X,  data.y, verbose=4)
            meanAccuracy.append(accuracy)

        meanAccuracy = np.array(meanAccuracy)
        acc = np.mean(meanAccuracy)
        print(f"Accuracy of : {amount} tests: {acc}")

def makeNewNeuralNetwork():
    nn = NeuralNetwork()
    nn.create()
    trainData = Data()
    trainData.loadDataFromFile("./data/data-1-100/train1100.txt")
    testData = Data()
    testData.loadDataFromFile("./data/data-1-100/test1100.txt")
    nn.train(trainData)
    nn.test(testData)
    nn.save()

def loadAndTestOldNetwork():
    nn = NeuralNetwork()
    nn.load()
    testData = Data()
    testData.loadDataFromFile("./data/data-1-100/test1100.txt")
    nn.test(testData)

def loadNetwork():
    nn = NeuralNetwork()
    nn.load()
    return nn



loadAndTestOldNetwork()
# makeNewNeuralNetwork()



#need strict pattern regonizer
#need ai sequental model
#need numberheatmap for input system.
#can i determine wheter user uses numpad or keyboard