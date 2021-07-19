def part1():
    with open('input3.txt', 'r') as input:
        steps = input.readline()

    visited = {}
    x, y = 0, 0

    visit(x, y, visited)

    for step in steps:
        xInc, yInc = getStepSize(step)

        x += xInc
        y += yInc

        visit(x, y, visited)
    
    print(len(visited))

def part2():
    with open('input3.txt', 'r') as input:
        steps = input.readline()
    
    visited = {}
    xSanta, ySanta = 0, 0
    xRobot, yRobot = 0, 0

    turn = 1

    visit(xSanta, ySanta, visited)
    visit(xRobot, yRobot, visited)

    for step in steps:
        xInc, yInc = getStepSize(step) 
        
        if turn % 2 == 0:
           xRobot += xInc
           yRobot += yInc
           visit(xRobot, yRobot, visited)
        else:
            xSanta += xInc
            ySanta += yInc
            visit(xSanta, ySanta, visited)
        
        turn += 1
    
    print(len(visited))

def visit(x, y, visited):
    visited[(x, y)] = visited.get((x, y), 0) + 1

def getStepSize(step):
    if step == '^':
        return (0, 1)
    elif step == 'v':
        return (0, -1)
    elif step == '>':
        return (1, 0)
    elif step == '<':
        return (-1, 0)

    
part1()
part2()