import numpy as np
import nnfs
import pickle
from nnfs.datasets import spiral_data

def getData(trainingFile):
    numbers=[]
    X=[]
    y=[]
    f = open(str(trainingFile))

        

    #For each line
    # for line in f:
    #     elements = line.strip().split()
    #     for number in range(len(line)-5):



    #     # line = line[:-1]
    #     # for number in range(len(line)-3):
    #     #     y.append(int(line[-1]))
    #     #     line = line[:-1]
            
    #     #     tempX = []
    #     #     for i in line[-3:]:
    #     #         tempX.append(int(i))
    #     #     X.append(tempX)
    

    # return np.array(X),np.array(y)
    

class Layer:
    #Creates the layer
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons) #Generates a matrics mbased on normal curve with size input*neurons
        self.biases = np.zeros((1, n_neurons)) #Creates a 1d array with size netursns

    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.dot(input, self.weights) + self.biases #Dot product becasue its mulypling 2d matrices instead of loop

class ReLU:
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.maximum(0, inputs) #Calculate output values, #important to be able to trained to not increase loss

class Activation_Softmax:

    # Forward pass
    def forward(self, inputs):
        # Remember input values
        self.inputs = inputs

        # Get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1,
                                            keepdims=True))
        # Normalize them for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1,
                                            keepdims=True)

        self.output = probabilities

class Loss_CategoricalCrossentropy(Loss):

    # Forward pass
    def forward(self, y_pred, y_true):

        # Number of samples in a batch
        samples = len(y_pred)

        # Clip data to prevent division by 0
        # Clip both sides to not drag mean towards any value
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

        # Probabilities for target values -
        # only if categorical labels
        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[
                range(samples),
                y_true
            ]


        # Mask values - only for one-hot encoded labels
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(
                y_pred_clipped * y_true,
                axis=1
            )

        # Losses
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods

    # Backward pass
    def backward(self, dvalues, y_true):

        # Number of samples
        samples = len(dvalues)
        # Number of labels in every sample
        # We'll use the first sample to count them
        labels = len(dvalues[0])

        # If labels are sparse, turn them into one-hot vector
        if len(y_true.shape) == 1:
            y_true = np.eye(labels)[y_true]

        # Calculate gradient
        self.dinputs = -y_true / dvalues
        # Normalize gradient
        self.dinputs = self.dinputs / samples

class Activation_Softmax_Loss_CategoricalCrossentropy():

    # Creates activation and loss function objects
    def __init__(self):
        self.activation = Activation_Softmax()
        self.loss = Loss_CategoricalCrossentropy()

    # Forward pass
    def forward(self, inputs, y_true):
        # Output layer's activation function
        self.activation.forward(inputs)
        # Set the output
        self.output = self.activation.output
        # Calculate and return loss value
        return self.loss.calculate(self.output, y_true)

X,y = getData(trainingFile="./Python/datatrain.txt")

class NeuralNetwork():
    def createNeuralNetwork(self):
        #Create Layer 1 Layer 2
        self.layer1 = Layer(3,18) #3 Inputs 18 neurons
        self.activation = ReLU()

        self.layer2 = Layer(18,10)

        self.loss_activation = Activation_Softmax_Loss_CategoricalCrossentropy()

        self.optimizer = Optimizer_Adam(learning_rate=0.05, decay=5e-7)

        




