

def decodeSeatRow(position: str) -> int:
    rowFrom = 0
    rowTo = 127
    for i in range(0, 6):
        direction = position[i]
        diff = 2 ** (6 - i)
        if (direction == 'F'):
            rowTo -= diff
        elif (direction == 'B'):
            rowFrom += diff
        else:
            raise Exception("Wrong direction: " + direction)
    if (position[6] == 'F'):
        return rowFrom 
    elif (position[6] == 'B'):
        return rowTo
    else:
        raise Exception("Wrong direction: " + position[6])


def decodeSeatCol(position: str) -> int:
    colFrom = 0
    colTo = 7
    for i in range(0, 3):
        direction = position[7 + i]
        diff = 2 ** (2 - i)
        if (direction == 'R'):
            colFrom += diff
        elif (direction == 'L'):
            colTo -= diff
        else:
            raise Exception("Wrong direction: " + direction)
    
    if (position[9] == 'R'):
        return colTo
    elif (position[9] == 'L'):
        return colFrom 
    else:
        raise Exception("Wrong direction: " + position[9])

def getSeatId(row, col):
    return row * 8 + col

def getSeatIds(lines):
    result = []
    for line in lines:
        line = line.strip()

        row = decodeSeatRow(line)
        col = decodeSeatCol(line)
        id = getSeatId(row, col)
        result.append(id)
    return result

input_file = open("2020/day5.input", "r")
content_list = input_file.readlines()
seatIds = getSeatIds(content_list)
maxSeatId = max(seatIds)

print(maxSeatId)