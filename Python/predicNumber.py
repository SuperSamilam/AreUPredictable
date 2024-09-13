import tensorflow as tf
from tensorflow import keras
import numpy as np

class Data():
    def loadDataFromFile(self, filename, depth = 3):
        self.X = []
        self.y = []

        with open(filename, 'r') as file:
            self.data = file.read()

        self.setupData(depth)

    def makeRandomDataSet(self, depth):
        self.X = []
        self.y = []
        self.data = ""
        for i in range(100):
            self.data += str(np.random.randint(0, 10))
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
        self.model = tf.keras.models.load_model('predictionmodel.keras')

    def create(self):
        self.model = tf.keras.Sequential()
        self.model.add(tf.keras.layers.Dense(units=20, activation='relu', input_dim=3))
        self.model.add(tf.keras.layers.Dense(units=10, activation='relu'))
        self.model.add(tf.keras.layers.Dense(units=10, activation='softmax'))

        opt = keras.optimizers.Adam(learning_rate=0.05)

        self.model.compile(optimizer='adam',
                    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                    metrics=['accuracy'])
    
    def train(self, data):
       self. model.fit(data.X, data.y, epochs=2000)

    def test(self, data):
        loss, accuracy = self.model.evaluate(data.X,  data.y, verbose=2)
        # print(f"Loss: {loss} Accuracy: {accuracy}")

    def save():
        self.model.save('predictionmodel.keras')

nn = NeuralNetwork()
#nn.create()
nn.load()
data = Data()
data.makeRandomDataSet(3)
nn.test(data)




#need strict pattern regonizer
#need ai sequental model
#need numberheatmap for input system.
#can i determine wheter user uses numpad or keyboard