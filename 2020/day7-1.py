
# light red bags contain 1 bright white bag, 2 muted yellow bags.

def readRules(lines):
    result = dict()
    for line in lines:
        line = line.strip()
        split = line.split(" contain ")
        container = split[0]
        containees = split[1].replace('.', '').split(", ")
        for content in containees:
            content = content.split(" ", 1)
            if content[1] not in result.keys():
                result[content[1]] = []
            result[content[1]].append([content[0], container])

    return result

def findOutermostBags(rules, bagColor):
    # TODO
    print("not done yet")

input_file = open("2020/day7-dummy.input", "r")
content_list = input_file.readlines()
rules = readRules(content_list)
print(rules)