
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


def calculate_waypoint_turn(waypointCoords: list[int], turn_direction: str, turn_step: int) -> str:
    result = None

    if turn_step == 270:
        turn_step = 90
        turn_direction = 'L' if turn_direction == 'R' else 'R'

    if turn_step == 180:
        result = [waypointCoords[0] * -1, waypointCoords[1] * -1]
    elif turn_step == 90:
        if turn_direction == 'L':
            result = [waypointCoords[1] * -1, waypointCoords[0]]
        elif turn_direction == 'R':
            result = [waypointCoords[1], waypointCoords[0] * -1]

    return result


def findFinalCoords(directions: list[str, int]):
    ferryCoords = [0, 0]
    waypointCoords = [10, 1]

    for d in directions:
        if d[0] in ['R', 'L']:
            waypointCoords = calculate_waypoint_turn(
                waypointCoords, d[0], d[1])
        elif d[0] == 'F':
            for i in range(0, d[1]):
                ferryCoords[0] += waypointCoords[0]
                ferryCoords[1] += waypointCoords[1]
        else:
            waypointCoords = DIRECTIONS_COUNTERS[d[0]](
                waypointCoords[0], waypointCoords[1], d[1])
    return ferryCoords


input_file = open("2020/12/day12.input", "r")
content_list = list(map(parse_direction, input_file.readlines()))
finalCoords = findFinalCoords(content_list)
print(finalCoords)
result = sum(map(abs, finalCoords))
print(result)
