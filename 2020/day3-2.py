
def findSymbolAtIndex(line: str, index: int):
    lineLen = len(line)
    calculatedIndex = index % lineLen
    result = line[calculatedIndex]
    # print(line, lineLen, index, calculatedIndex, result)
    return result

def trySlope(slopeMap, xDelta, yDelta):
    xCoords = 0
    yCoords = 0
    treeCount = 0

    while (yCoords < len(slopeMap) - 1):
        xCoords += xDelta
        yCoords += yDelta
        line = slopeMap[yCoords].strip()
        mapSymbol = findSymbolAtIndex(line, xCoords)
        # print(xCoords, yCoords, mapSymbol)

        if (mapSymbol == '#'):
            treeCount += 1
    return treeCount

input_file = open("2020/day3.input", "r")
content_list = input_file.readlines()

slopeDeltas = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2],
]

results = []

for delta in slopeDeltas:
    subresult = trySlope(content_list, delta[0], delta[1])
    results.append(subresult)

finalResult = 1
for r in results:
    finalResult *= r

print(finalResult)
