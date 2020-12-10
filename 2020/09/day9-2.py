
def loadNumbers(content_lines):
    numbers_list = []

    for line in content_list:
        numbers_list.append(int(line))

    print("loaded numbers: ", len(numbers_list))
    return numbers_list


def findContiguousSetForNumber(numbers_list, invalid_number):
    for i in range(0, len(numbers_list)):
        sumOfSet = 0
        setOfNumbers = set([])
        for j in range(i, len(numbers_list)):
            number = numbers_list[j]

            if (number == invalid_number):
                raise Exception("Reached invalid_number :(")

            sumOfSet += number

            if sumOfSet > invalid_number:
                break

            setOfNumbers.add(number)

            if sumOfSet == invalid_number:
                return setOfNumbers


INVALID_NUMBER = 731031916
input_file = open("2020/day9.input", "r")
content_list = input_file.readlines()
numbers_list = loadNumbers(content_list)

setOfNumbers = findContiguousSetForNumber(numbers_list, INVALID_NUMBER)
result = min(setOfNumbers) + max(setOfNumbers)

print(result)
