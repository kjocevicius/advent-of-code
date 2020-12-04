
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