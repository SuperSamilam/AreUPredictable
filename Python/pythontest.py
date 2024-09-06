import numpy
import pandas as pd

#this code is not mine, this is from a tutorial on machine learning i did to learn machine learning
music_data = pd.read_csv('Python/music.csv')
X = music_data.drop(columns=['genre'])
Y = music_data['genre']

# print("hej")
print(X)