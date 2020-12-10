

def find_combinations(numbers: list[int], targetJolt: int, currentJolt: int = 0, lastAdapterIndex: int = 0):
    nextAdapterIndex = lastAdapterIndex
    combinations = 0

    while True:
        nextAdapterIndex += 1

        if nextAdapterIndex >= len(numbers):
            break

        nextJolt = numbers[nextAdapterIndex]
        nextJoltDiff = nextJolt - currentJolt

        if nextJoltDiff > 3:
            break
        elif nextJolt == targetJolt:
            combinations += 1
        else:
            combinations += find_combinations(numbers,
                                              targetJolt, nextJolt, nextAdapterIndex)

    return combinations


input_file = open("2020/10/day10.input", "r")
content_list = input_file.readlines()
numbers_list = list(map(int, content_list))
numbers_list.sort()
numbers_list.insert(0, 0)

max_jolt = max(numbers_list)
combinations = find_combinations(numbers_list, max_jolt)
print(combinations)
