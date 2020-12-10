

def find_combinations(numbers: list[int], targetJolt: int, currentJoltIndex: int = 0):
    currentJolt = numbers[currentJoltIndex]
    nextJoltIndex = currentJoltIndex
    combinations = 0

    while True:
        nextJoltIndex += 1

        if nextJoltIndex >= len(numbers):
            break

        nextJolt = numbers[nextJoltIndex]
        nextJoltDiff = nextJolt - currentJolt

        if nextJoltDiff > 3:
            break
        elif nextJolt == targetJolt:
            combinations += 1
        else:
            combinations += find_combinations(numbers,
                                              targetJolt, nextJoltIndex)

    return combinations


PREAMBLE_LEN = 25
input_file = open("2020/10/day10-dummy2.input", "r")
content_list = input_file.readlines()
numbers_list = list(map(int, content_list))
numbers_list.sort()

max_jolt = max(numbers_list)
combinations = find_combinations(numbers_list, max_jolt)
print(combinations)
