
def parseFile():
    with open('input/input5.txt', 'r') as file:
        lines = [line.strip() for line in file]
        rules = dict()
        i = 0
        while lines[i] != '':
            y = int(lines[i][:lines[i].find('|')])
            x = int(lines[i][lines[i].find('|')+1:])
            if x in rules:
                rules[x].add(y)
            else:
                rules[x] = {y}
            i += 1

        i += 1
        updates = [[int(n) for n in line.split(',')] for line in lines[i:]]

        return rules, updates

def part1(rules, updates):
    total = 0

    for update in updates:
        ordered = True
        for i in range(len(update)):
            if update[i] in rules:
                rule = rules[update[i]]
                if set(rule) & set(update[i+1:]):
                    ordered = False
                    break
        if ordered:
            total += update[len(update)//2]

    return total

def order(update, rules):
    newList = []
    nums = set(update)

    rulesList = [set() if n not in rules else rules[n] & nums for n in update]

    while update:
        for i in range(len(update)):
            if not rulesList[i]:
                newList.append(update[i])
                rulesList = rulesList[:i] + rulesList[i+1:]
                rulesList = [r - {update[i]} for r in rulesList]
                update = update[:i] + update[i+1:]
                break

    return newList


def part2(rules, updates):
    total = 0

    for update in updates:
        ordered = True
        for i in range(len(update)):
            if update[i] in rules:
                rule = rules[update[i]]
                if rule & set(update[i+1:]):
                    ordered = False
                    break
        if not ordered:
            total += order(update, rules)[len(update)//2]

    return total


rules, updates = parseFile()
# print(part1(rules, updates))
print(part2(rules, updates))

