
def calc_next_bus_time(timestamp: int, bus_id: int):
    previous_bus_time = int(timestamp / bus_id) * bus_id
    next_bus_time = previous_bus_time + bus_id
    return next_bus_time


input_file = open("2020/13/day13.input", "r")
content_list = input_file.readlines()
timestamp = int(content_list[0])
bus_lines = list(
    map(int, filter(lambda v: v.isdigit(), content_list[1].split(','))))
next_bus_times = list(
    map(lambda v: calc_next_bus_time(timestamp, v), bus_lines))
print(timestamp, bus_lines)
print(next_bus_times)

least_minutes_to_wait = min(next_bus_times)
least_minutes_to_wait_bus_line = bus_lines[next_bus_times.index(
    least_minutes_to_wait)]
minutes_to_wait = least_minutes_to_wait - timestamp
result = least_minutes_to_wait_bus_line * minutes_to_wait
print(result)
