
# light red bags contain 1 bright white bag, 2 muted yellow bags.

def readRules(lines):
    result = dict()
    for line in lines:
        line = line.strip().replace(" bags", "").replace(" bag", "")
        split = line.split(" contain ")
        container = split[0]
        containees = split[1].replace('.', '').split(", ")
        for content in containees:
            content = content.split(" ", 1)
            if content[1] not in result.keys():
                result[content[1]] = []
            result[content[1]].append([content[0], container])

    return result

def findOutermostBagsColors(rules, bagColor, depth = 0, outerColors = set([])):
    nextDepth = depth + 1

    if depth > 0:
        outerColors.add(bagColor)

    if (bagColor in rules):
        containers = rules[bagColor]
        for c in containers:
            if c[0] == "no" or int(c[0]) == 0:
                continue
            
            findOutermostBagsColors(rules, c[1], nextDepth, outerColors)

    return outerColors

myBagColor = "shiny gold"
input_file = open("2020/day7.input", "r")
content_list = input_file.readlines()
rules = readRules(content_list)
# print(rules, myBagColor)
outermostColors = findOutermostBagsColors(rules, myBagColor)
print(len(outermostColors))