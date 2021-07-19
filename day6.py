import re

parser = re.compile('(turn on|turn off|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)')

def parts():
    with open('input6.txt', 'r') as input:

        grid1 = {}
        grid2 = {}

        for line in input:
            parts = parser.match(line)
            instr = parts.group(1)
            start = (int(parts.group(2)), int(parts.group(3)))
            end = (int(parts.group(4)), int(parts.group(5)))

            for x in range(start[0], end[0] + 1):
                for y in range(start[1], end[1] + 1):
                    if instr == 'turn on':
                        grid1[(x, y)] = 1
                        grid2[(x, y)] = grid2.get((x, y), 0) + 1
                    elif instr == 'turn off':
                        grid1[(x, y)] = 0
                        grid2[(x, y)] = max(0, grid2.get((x, y), 0) - 1)
                    elif instr == 'toggle':
                        grid1[(x, y)] = grid1.get((x, y), 0) ^ 1
                        grid2[(x, y)] = grid2.get((x, y), 0) + 2

        numOn = 0

        for state in grid1.values():
            if state == 1:
                numOn += 1

        total = 0
        for state in grid2.values():
            total += state

        print(f"Part 1: {numOn}")
        print(f"Part 2: {total}")

parts()