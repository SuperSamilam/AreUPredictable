import tensorflow as tf
from tensorflow import keras1
import numpy as np
import Data as data

class NeuralNetwork():
    def create(self, depth, neurons):
        self.model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=(depth,)),
        tf.keras.layers.Dense(neurons, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax"),
        ])

        self.model.compile(optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])
        
    def train(self, data, epochs):
       self. model.fit(data.X, data.y, epochs=epochs)

    def test(self, data):
        self.loss, self.accuracy = self.model.evaluate(data.X,  data.y, verbose=2)

    def ctt(self, depth, neurons, train, test, epochs):
        self.create(depth, neurons)
        self.train(train, epochs)
        self.test(test)

    def predictRaw(self, inputdata):
        prediction = self.model.predict(inputdata)
        return prediction
    
    def predict(self, inputdata):
        prediction = self.model.predict(inputdata)
        return np.argmax(prediction, axis=1)
    
    def load(self, modelName):
        self.model = tf.keras.models.load_model('./models/' + modelName + '.keras')
        # self.model = tf.keras.models.load_model("./models/" + modelName + '.keras')

    def save(self, modelName, neurons, depth):
        self.model.save("./models/" + modelName + '.keras')
        with open("./models/" + modelName + ".txt", 'w') as file:
            pass
        indent = "    "
        with open("./models/" + modelName + ".txt", 'w') as file:
            file.write(f"Model: {modelName} \n \n")
            file.write(f"{indent} Accuracy: {self.accuracy}\n")
            file.write(f"{indent} Loss: {self.loss}\n \n")

            file.write(f"{indent} Depth: {depth}\n")
            file.write(f"{indent} NeuronLayers: input 3, {neurons} relu, 10 softmax \n \n")

    def websave(self, modelName):
        self.model.save("./models/web" + modelName)

    def runRandomTests(self, amount, depth):
        meanAccuracy = []
        for i in range(amount):
            data = data.Data()
            data.makeRandomDataSet(depth)
            loss, accuracy = self.model.evaluate(data.X,  data.y, verbose=4)
            meanAccuracy.append(accuracy)

        meanAccuracy = np.array(meanAccuracy)
        acc = np.mean(meanAccuracy)
        print(f"Accuracy of : {amount} tests: {acc}")