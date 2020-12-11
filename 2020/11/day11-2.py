
directions_counters = [
    lambda x, y, delta: [x - delta, y],  # <-
    lambda x, y, delta: [x + delta, y],  # ->
    lambda x, y, delta: [x, y - delta],  # /\
    lambda x, y, delta: [x, y + delta],  # \/
    lambda x, y, delta: [x + delta, y - delta],  # /^
    lambda x, y, delta: [x - delta, y - delta],  # ^\
    lambda x, y, delta: [x - delta, y + delta],  # _/
    lambda x, y, delta: [x + delta, y + delta],  # \_
]


def calculate_adjacent_taken_pos(plane_map: list[list], x, y):
    occupied_seats = 0
    for directionInc in directions_counters:
        delta = 0
        visibleSeat = None
        while (visibleSeat in [None, '.']):
            delta += 1
            coords = directionInc(x, y, delta)

            if coords[0] < 0 or coords[0] >= len(plane_map[y]) or coords[1] < 0 or coords[1] >= len(plane_map):
                break

            visibleSeat = plane_map[coords[1]][coords[0]]

        if visibleSeat == '#':
            occupied_seats += 1

    return occupied_seats


def switching_round(plane_map: list[list]):
    plane_map_copy = list(map(lambda l: l.copy(), plane_map))
    changes_count = 0
    for x in range(0, len(plane_map_copy[0])):
        for y in range(0, len(plane_map_copy)):
            status = plane_map_copy[y][x]

            if status == '.':
                continue

            occupied_seats = calculate_adjacent_taken_pos(plane_map_copy, x, y)

            if status == 'L' and occupied_seats == 0:
                plane_map[y][x] = '#'
                changes_count += 1
            elif status == '#' and occupied_seats >= 5:
                plane_map[y][x] = 'L'
                changes_count += 1

    return changes_count


def print_map(plane_map: list[list[str]]):
    for line in plane_map:
        print("".join(line))


def solve(plane_map: list[list]):

    while True:
        changes_count = switching_round(plane_map)
        # print("---")
        # print("Changes: ", changes_count)
        # print_map(plane_map)
        if changes_count == 0:
            break

    occupied_count = 0
    for x in range(0, len(plane_map[0])):
        for y in range(0, len(plane_map)):
            status = plane_map[y][x]
            if status == '#':
                occupied_count += 1

    return occupied_count


input_file = open("2020/11/day11.input", "r")
content_list = list(map(lambda l: list(l.strip()), input_file.readlines()))
result = solve(content_list)
print(result)
