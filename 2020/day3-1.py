
def findSymbolAtIndex(line: str, index: int):
    lineLen = len(line)
    calculatedIndex = index % lineLen
    result = line[calculatedIndex]
    # print(line, lineLen, index, calculatedIndex, result)
    return result

input_file = open("2020/day3.input", "r")
content_list = input_file.readlines()

xCoords = 0
yCoords = 0
treeCount = 0

while (yCoords < len(content_list) - 1):
    xCoords += 3
    yCoords += 1
    line = content_list[yCoords].strip()
    mapSymbol = findSymbolAtIndex(line, xCoords)
    # print(xCoords, yCoords, mapSymbol)

    if (mapSymbol == '#'):
        treeCount += 1

print(treeCount)
