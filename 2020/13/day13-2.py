
def solve_silly(bus_lines: list):

    result = None
    base_line_id = bus_lines[0]
    time = 0

    while result == None:
        time += base_line_id
        successes = 0

        for i in range(1, len(bus_lines)):
            bus_line = bus_lines[i]
            if (bus_line is not int):
                continue

            subtime = time + i
            mod = subtime % bus_line
            if mod != 0:
                break
            else:
                successes += 1

        if successes == len(bus_lines) - 2:
            result = time

    return result


input_file = open("2020/13/day13-dummy.input", "r")
content_list = input_file.readlines()
bus_lines = list(
    map(lambda v: int(v) if v.isdigit() else v, content_list[1].split(',')))
solve_silly(bus_lines)
