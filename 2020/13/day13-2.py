
def calc_next_bus_time(timestamp: int, bus_id: int):
    previous_bus_time = int(timestamp / bus_id) * bus_id
    next_bus_time = previous_bus_time + bus_id
    return next_bus_time


input_file = open("2020/13/day13.input", "r")
content_list = input_file.readlines()
bus_lines = list(
    map(int, filter(lambda v: v.isdigit(), content_list[1].split(','))))
next_bus_times = list(
    map(lambda v: calc_next_bus_time(timestamp, v), bus_lines))
print(timestamp, bus_lines)
print(next_bus_times)
