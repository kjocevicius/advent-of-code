

def executeProgramUntilRepeat(program):
    programPointer = 0
    acc = 0

    programPointerHistory = set([])

    while (programPointer not in programPointerHistory):
        programPointerHistory.add(programPointer)
        command = program[programPointer].split(" ")

        if command[0] == "nop":
            programPointer += 1
        elif command[0] == "jmp":
            delta = int(command[1])
            programPointer += delta
        elif command[0] == "acc":
            delta = int(command[1])
            acc += delta
            programPointer += 1

    return acc


input_file = open("2020/day8.input", "r")
content_list = input_file.readlines()
result = executeProgramUntilRepeat(content_list)

print(result)
