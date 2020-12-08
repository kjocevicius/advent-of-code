
# light red bags contain 1 bright white bag, 2 muted yellow bags.

def readRules(lines):
    result = dict()
    for line in lines:
        line = line.strip().replace(" bags", "").replace(" bag", "")
        split = line.split(" contain ")
        container = split[0]
        containees = split[1].replace('.', '').split(", ")
        containeesSplit = []
        for content in containees:
            containeesSplit.append(content.split(" ", 1))
        result[container] = containeesSplit

    return result

def calculateBags(rules, bagColor, depth = 0):
    result = 0

    if depth > 0:
        result += 1

    innerRules = rules[bagColor]

    for rule in innerRules:
        if rule[0] == "no":
            continue
        times = int(rule[0])
        bagInnerCount = calculateBags(rules, rule[1], depth + 1)
        result += times * bagInnerCount

    return result


myBagColor = "shiny gold"
input_file = open("2020/day7.input", "r")
content_list = input_file.readlines()
rules = readRules(content_list)
# print(rules, myBagColor)
bagsCount = calculateBags(rules, myBagColor)
print(bagsCount)