import random
import pickle

thisList = [0]
RandTxt = "Random number {} within range (0:10): {}"
counter = 0
for a in range(0,10000,1):
        randomResult = random.randrange(0,10,1)
        thisList.insert((a), randomResult)
        print(RandTxt.format((a),randomResult))

thisListNum = len(thisList)
thisList.pop(-1)

print("Number of objects in list: ")
print(thisListNum)
print(thisList)

'''
f = open("C:\\Users\scowley\OneDrive - Wichita State University\Coding\Python\Projects\generator\genNums.txt")
print(f.read())
f.close()

with open("C:\\Users\scowley\OneDrive - Wichita State University\Coding\Python\Projects\generator\genNums.txt", 'a') as file_handler:
        for item in thisList:
                file_handler.write("{} ".format(item))
                */
'''                