# drinkFile = open("ch05/drinks.txt")

# print(drinkFile.readlines())
# print(drinkFile.read().rsplit())

# drinkFile.close()

drinkFile = open("ch05/drinks.txt")

# print(drinkFile.readline())
# print(drinkFile.readline())
# print(drinkFile.readline())

hasValues = True
resultList = []
while hasValues:
    line = drinkFile.readline()
    if line != "":
        # print(line)
        resultList.append(line.strip())
    else:
        hasValues = False

print(resultList)
