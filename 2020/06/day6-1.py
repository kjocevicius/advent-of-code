
from typing import Set


def readGroups(lines: list[str]) -> list[set]:
    
    groups: list = []
    group = set()

    for line in lines:
        line = line.strip()

        if len(line) == 0:
            groups.append(group)
            group = set()
            continue

        for letter in line:
            group.add(letter)
            
    groups.append(group)
    return groups

def sumGroupAnswers(groups: list[set]) -> int:
    result = 0
    for group in groups:
        result += len(group)
    return result

input_file = open("2020/day6.input", "r")
content_list = input_file.readlines()
groups = readGroups(content_list)
sum = sumGroupAnswers(groups)

print(sum)