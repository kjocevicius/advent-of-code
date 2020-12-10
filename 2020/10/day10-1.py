
def loadNumbers(content_lines):
    numbers_list = []

    for line in content_list:
        numbers_list.append(int(line))

    print("loaded numbers: ", len(numbers_list))
    return numbers_list


PREAMBLE_LEN = 25
input_file = open("2020/10/day10.input", "r")
content_list = input_file.readlines()
numbers_list = loadNumbers(content_list)


print(numbers_list)
