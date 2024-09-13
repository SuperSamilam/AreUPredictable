#This file is mainly for being able to find datasets of different structurs and convert it to my structure
#Currently I have found 2 datasets I can use and therefor only impemented theese types of sturcutes

filename = "./data/test/test09.txt"

#Structure 1 
# 161906326230734734 
# Should become
# 1, 6, 1, 9, 0, 6, 3, 2, 6, 2, 3, 0, 7 ect

#Reads file
with open(filename, 'r') as file:
    data = file.read()

#Clears file
with open(filename, 'w') as file:
    pass

with open(filename, 'w') as file:
    for char in data:
        file.write(char + ", ")


#Structure 2 not only single digits
# 50, 04, 81, 40, 02 ect
#Should become
# 50, 4, 81, 40, 2