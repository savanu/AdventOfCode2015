
def part1():
    with open('input1.txt', 'r') as input:
        steps = input.readline()

    floor = 0

    for step in steps:
        if step == '(':
            floor += 1
        elif step == ')':
            floor -= 1

    print(floor)

def part2():
    with open('input1.txt', 'r') as input:
        steps = input.readline()
    
    floor = 0
    pos = 0

    while (floor >= 0):
        step = steps[pos]
        if step == '(':
            floor += 1
        elif step == ')':
            floor -= 1
        pos += 1
    
    print(pos)

part2()
