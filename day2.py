
def part1():
    with open('input2.txt', 'r') as input:
        lines = input.readlines()

    total = 0

    for line in lines:
        (l, w, h) = [int(x) for x in line.split('x')]
        side1 = l*w
        side2 = w*h
        side3 = h*l

        total += 2*side1 + 2*side2 + 2*side3 + min(side1, side2, side3)
    
    print(total)

def part2():
    with open('input2.txt', 'r') as input:
        lines = input.readlines()

    total = 0

    for line in lines:
        (l, w, h) = sorted([int(x) for x in line.split('x')])
        
        total += (2*l + 2*w) + (l*w*h)
    
    print(total)

part2()