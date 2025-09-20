
def parseFile():
    with open('input/input17.txt') as file:
        lineA = file.readline()
        regA = int(lineA[lineA.find(':') + 2:])
        lineB = file.readline()
        regB = int(lineB[lineB.find(':') + 2:])
        lineC = file.readline()
        regC = int(lineC[lineC.find(':') + 2:])

        file.readline()

        lineP = file.readline()
        program = [int(d) for d in lineP[lineP.find(':') + 2:].split(',')]

        return regA, regB, regC, program

def part1(regA, regB, regC, program):
    def getComboValue(operand):
        match operand:
            case 4:
                return regA
            case 5:
                return regB
            case 6:
                return regC
            case _:
                return operand

    outputValue = False
    pc = 0

    while pc < len(program):
        operand = program[pc + 1]

        match program[pc]:
            case 0:
                regA //= (2 ** getComboValue(operand))
            case 1:
                regB ^= operand
            case 2:
                regB = getComboValue(operand) % 8
            case 3 if regA != 0:
                pc = operand - 2
            case 4:
                regB ^= regC
            case 5:
                if outputValue:
                    print(',', end='')
                else:
                    outputValue = True
                print(getComboValue(operand) % 8, end='')
            case 6:
                regB = regA // (2 ** getComboValue(operand))
            case 7:
                regC = regA // (2 ** getComboValue(operand))

        pc += 2

    print()

def part2(regBOriginal, regCOriginal, program):
    def findNext(program, regA):
        if not program:
            return regA

        for x in range(8):
            if (x ^ 6 ^ ((regA * 8 + x) // (2 ** (x ^ 6))) ^ 7) % 8 == program[-1]:
                if (finalRegA := findNext(program[:-1], regA * 8 + x)) is not None:
                    return finalRegA

        return None

    return findNext(program, 0)

regA, regB, regC, program = parseFile()
# part1(regA, regB, regC, program)
print(part2(regB, regC, program))

