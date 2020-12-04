
import re

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) - OPTIONAL

REQUIRED_PROP_TYPES = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    #"cid",
]

COLOR_PATTERN = re.compile("\#([0-9a-f]){6}")
EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth",]

def isBetween(v, v1, v2):
    return v >= v1 and v <= v2

def validateHgt(v: str):
    if v.endswith("cm"):
        h = v.replace("cm", "")
        return h.isdigit() and isBetween(int(h), 150, 193)
    if v.endswith("in"):
        h = v.replace("in", "")
        return h.isdigit() and isBetween(int(h), 59, 76)
    print("validateHgt, bad data: v")
    return False

VALIDATION_RULES = {
    "byr": lambda v : len(v) == 4 and v.isdigit() and isBetween(int(v), 1920, 2002),
    "iyr": lambda v : len(v) == 4 and v.isdigit() and isBetween(int(v), 2010, 2020),
    "eyr": lambda v : len(v) == 4 and v.isdigit() and isBetween(int(v), 2020, 2030),
    "hgt": validateHgt,
    "hcl": lambda v : len(v) == 7 and re.match(COLOR_PATTERN, v) is not None,
    "ecl": lambda v : v in EYE_COLORS,
    "pid": lambda v : len(v) == 9 and v.isdigit(),
    "cid": lambda v : True
}

def parsePassports(lines):
    passports = []
    passport = {}


    for line in lines:
        line = line.strip()

        if len(line) > 0:
            props = line.split(' ')
            for prop in props:
                splitProp = prop.split(':')
                passport[splitProp[0]] = splitProp[1]
        else:
            passports.append(passport)
            passport = {}
    
    passports.append(passport)
    return passports

def validatePassport(passport: dict):
    for k in REQUIRED_PROP_TYPES:
        if k not in passport:
            return False
        
        validationRule = VALIDATION_RULES[k]
        isValid = validationRule(passport[k])
        if (not isValid):
            print("Key invalid: ", k, passport[k])
            return False
        
    # print('---')
    return True

input_file = open("2020/day4.input", "r")
content_list = input_file.readlines()

passports = parsePassports(content_list)
validPassports = []

for p in passports:
    isValid = validatePassport(p)
    if isValid:
        validPassports.append(p)

print(len(validPassports))