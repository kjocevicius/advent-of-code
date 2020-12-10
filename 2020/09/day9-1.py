
def loadNumbers(content_lines):
    numbers_list = []

    for line in content_list:
        numbers_list.append(int(line))

    print("loaded numbers: ", len(numbers_list))
    return numbers_list


def isValidNumber(number, numbers_list, pre_range):
    for i in pre_range:
        for j in pre_range:
            if i == j:
                continue

            sum = numbers_list[i] + numbers_list[j]

            if number == sum:
                return True
    return False


def validateNumbers(numbers_list, preamble_len):
    for i in range(preamble_len, len(numbers_list)):
        number_to_validate = numbers_list[i]
        pre_range = range(i - preamble_len, i)
        result = isValidNumber(number_to_validate, numbers_list, pre_range)

        if not result:
            return numbers_list[i]


PREAMBLE_LEN = 25
input_file = open("2020/day9.input", "r")
content_list = input_file.readlines()
numbers_list = loadNumbers(content_list)

invalidNumber = validateNumbers(numbers_list, PREAMBLE_LEN)

print(invalidNumber)
