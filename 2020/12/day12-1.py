
# N = y+
# S = y-
# E = x+
# W = x-

DIRECTIONS = ['E', 'S', 'W', 'N']
DIRECTIONS_REV = DIRECTIONS.copy()
DIRECTIONS_REV.reverse()

DIRECTIONS_COUNTERS = {
    'E': lambda x, y, delta: [x + delta, y],  # <-
    'W': lambda x, y, delta: [x - delta, y],  # ->
    'N': lambda x, y, delta: [x, y + delta],  # /\
    'S': lambda x, y, delta: [x, y - delta],  # \/
}


def parse_direction(line: str) -> list[str, int]:
    direction = line[0]
    step = int(line[1:])
    return [direction, step]


def calculate_turn(direction: str, turn_direction: str, turn_step: int) -> str:
    turns = int(turn_step / 90)
    turnStarted = False
    newDirection = None
    directions = DIRECTIONS if turn_direction == 'R' else DIRECTIONS_REV
    while(turns != 0):
        for d in directions:
            if not turnStarted and d == direction:
                turnStarted = True
            elif turnStarted:
                turns -= 1
                if turns == 0:
                    newDirection = d
                    break

    return newDirection


def findFinalCoords(directions: list[str, int]):
    ferryCoords = [0, 0]
    ferryDirection = 'E'

    for d in directions:
        if d[0] in ['R', 'L']:
            ferryDirection = calculate_turn(ferryDirection, d[0], d[1])
        elif d[0] == 'F':
            ferryCoords = DIRECTIONS_COUNTERS[ferryDirection](
                ferryCoords[0], ferryCoords[1], d[1])
        else:
            ferryCoords = DIRECTIONS_COUNTERS[d[0]](
                ferryCoords[0], ferryCoords[1], d[1])

    return ferryCoords


input_file = open("2020/12/day12.input", "r")
content_list = list(map(parse_direction, input_file.readlines()))
finalCoords = findFinalCoords(content_list)
print(finalCoords)
result = sum(map(abs, finalCoords))
print(result)
