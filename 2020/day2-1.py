
class PasswordData(object):
    password: str = ""
    policyLetter: str = ""
    policyMinLetters: int = 0
    policyMaxLetters: int = 0

def parse_passwords(lines):
    result = []
    for line in lines: 
        passwordData = PasswordData()

        splitStrings = line.split(': ')
        policy = splitStrings[0]
        passwordData.password = splitStrings[1]
        
        splitStrings = policy.split(' ')
        passwordData.policyLetter = splitStrings[1]
        
        splitStrings = splitStrings[0].split('-')
        passwordData.policyMinLetters = int(splitStrings[0])
        passwordData.policyMaxLetters = int(splitStrings[1])
        result.append(passwordData)
    return result

def solve(passwordDatas):
    result = []
    for passwordData in passwordDatas:
        policyLetterCount = passwordData.password.count(passwordData.policyLetter)
        if policyLetterCount <= passwordData.policyMaxLetters and policyLetterCount >= passwordData.policyMinLetters:
            result.append(passwordData)

    return result


input_file = open("day2.input", "r")
content_list = input_file.readlines()
passwordsData = parse_passwords(content_list)
result = solve(passwordsData)

print(len(result))