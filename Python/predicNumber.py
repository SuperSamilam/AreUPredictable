#need strict pattern regonizer
#need ai sequental model
#need numberheatmap for input system.
#can i determine wheter user uses numpad or keyboard

import tensorflow as tf
from tensorflow import keras
import numpy as np



X = []
y = []
data = ""
print("Setting up data")
# with open("neo.txt", 'r') as file:
#         data = file.read() 
        
for i in range(100):
    data += str(np.random.randint(0, 10))
    
    


print("DATA IS READ")
i = 4
while i < len(data):
    label = int(data[i])
    j = i - 4
    features = list(data[j:j+3])
    try:
        features = [int(x) for x in features]
    except ValueError:
        print("DU ÄR BAJS")
    X.append(features)
    y.append(label)
    i += 1
    
X = np.array(X)
y = np.array(y)
    
X_test = []
y_test = []

print("Setting up data")
with open("sam.txt", 'r') as file:
        data = file.read() 

data = ""
for i in range(100):
    data += str(np.random.randint(0, 10))

print("DATA IS READ")
i = 4
while i < len(data):
    label = int(data[i])
    j = i - 4
    features = list(data[j:j+3])
    try:
        features = [int(x) for x in features]
    except ValueError:
        print("DU ÄR BAJS")
    X_test.append(features)
    y_test.append(label)
    i += 1
    
X_test = np.array(X)
y_test = np.array(y)

print("setting up model")
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=20, activation='relu', input_dim=3))
model.add(tf.keras.layers.Dense(units=10, activation='relu'))
model.add(tf.keras.layers.Dense(units=10, activation='softmax'))

print("set up optimizers")
opt = keras.optimizers.Adam(learning_rate=0.05)

print("Compeling")
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

print("Starting to fit")
model.fit(X, y, epochs=2000)
loss, accuracy = model.evaluate(X_test,  y_test, verbose=2)
print("fitted")
print(loss)
print(accuracy)