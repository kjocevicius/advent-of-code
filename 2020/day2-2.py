
class PasswordData(object):
    password: str = ""
    policyLetter: str = ""
    position1: str = ""
    position2: str = ""


def parse_passwords(lines: list):
    result = []
    for line in lines: 
        passwordData = PasswordData()

        splitStrings = line.split(': ')
        policy = splitStrings[0]
        passwordData.password = splitStrings[1]
        
        splitStrings = policy.split(' ')
        passwordData.policyLetter = splitStrings[1]
        
        splitStrings = splitStrings[0].split('-')
        passwordData.position1 = int(splitStrings[0]) - 1
        passwordData.position2 = int(splitStrings[1]) - 1
        result.append(passwordData)
    return result

def solve(passwordDatas: list):
    result = []
    for passwordData in passwordDatas:
        letterAt1 = passwordData.password[passwordData.position1]
        letterAt2 = passwordData.password[passwordData.position2]
        if (letterAt1 == passwordData.policyLetter or letterAt2 == passwordData.policyLetter) and letterAt1 != letterAt2:
            result.append(passwordData)

    return result


input_file = open("2020/day2.input", "r")
content_list = input_file.readlines()
passwordsData = parse_passwords(content_list)
result = solve(passwordsData)

print(len(result))