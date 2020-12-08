

def executeProgramUntilRepeat(program):
    programLen = len(program)
    programPointer = 0
    acc = 0

    programPointerHistory = []

    while (programPointer >= 0 and programPointer < programLen):
        if (programPointer in programPointerHistory):
            previousPointer = programPointerHistory[len(programPointerHistory)-1]
            return programPointerHistory

        programPointerHistory.append(programPointer)
        command = program[programPointer]
        command = command.split(" ")
        
        if command[0] == "nop":
            programPointer += 1
        elif command[0] == "jmp":
            delta = int(command[1])
            programPointer += delta
        elif command[0] == "acc":
            delta = int(command[1])
            acc += delta
            programPointer += 1
        else:
            raise Exception("Unknown command " + command)

    print("Program completed!", acc)
    return acc

def fixProgram(program, executionHistory):

    for commandIndex in executionHistory:
        command = program[commandIndex].strip()
        # print("Trying to fix command: ", commandIndex, command)
        if (command.startswith("jmp")):
            command = command.replace("jmp", "nop")
        elif command.startswith("nop"):
            command = command.replace("nop", "jmp")
        else:
            continue

        fixedProgram = program.copy()
        fixedProgram[commandIndex] = command

        fixedResult = executeProgramUntilRepeat(fixedProgram)

        if (fixedResult is not None and isinstance(fixedResult, int)):
            return fixedResult

    raise Exception("No success fixing program :(")


input_file = open("2020/day8.input", "r")
content_list = input_file.readlines()

executionHistory = executeProgramUntilRepeat(content_list)
result = fixProgram(content_list, executionHistory)

print(result)