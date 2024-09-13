
f = open("data.txt", "a")


for i in range(100):
    data = input()
    if (data.isnumeric() == False):
        if (data == 's'):
            print("stopping")
            break
        i-1
        continue
    data = int(data)
    if (0 <= data and data <= 9):
        f.write(str(data) + ", ")
        
f.close()

print("stopped")
