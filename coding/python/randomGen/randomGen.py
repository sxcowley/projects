import random
import pickle

thisList = [0]
RandTxt = "Random number {} within range (0:10): {}"
counter = 0
for a in range(0,1000,1):
        randomResult = random.randrange(0,10,1)
        thisList.insert((a), randomResult)
        print(RandTxt.format((a),randomResult))

thisListNum = len(thisList)
thisList.pop(-1)

print("Number of objects in list: ")
print(thisListNum)
print(thisList)

#'''
f = open(r'C:\\Users\\scowley\\Downloads\\genNums.txt')
print(f.read())
f.close()

with open('C:\\Users\\scowley\\Downloads\\genNums.txt', 'a+') as file_handler:
        for item in thisList:
                file_handler.write("{} ".format(item))
#'''                