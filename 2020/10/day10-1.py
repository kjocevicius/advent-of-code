
def get_diffs(numbers: list[int]) -> list[int]:
    result = []
    previous = numbers[0]
    for i in range(1, len(numbers)):
        v = numbers[i]
        result.append(v - previous)
        previous = v

    return result


PREAMBLE_LEN = 25
input_file = open("2020/10/day10.input", "r")
content_list = input_file.readlines()
numbers_list = list(map(int, content_list))
numbers_list.sort()
numbers_diffs = get_diffs(numbers_list)

jolts_1_count = numbers_diffs.count(1) + 1
jolts_3_count = numbers_diffs.count(3) + 1
jolts_multiplied = jolts_1_count * jolts_3_count

print(jolts_1_count, jolts_3_count)
print(jolts_multiplied)
