def part1():
    with open("inputs/input8.txt", "r") as input:
        lines = [line.rstrip() for line in input.readlines()]
    
    codeTotal = 0
    memTotal = 0

    prog = "length = len(%s)"
    gVars = {}

    for line in lines:
        codeTotal += len(line)
        gVars["length"] = 0
        exec(prog % line, gVars)
        memTotal += gVars["length"]
    
    print(f"Part 1: {codeTotal - memTotal}")

def part2():
    with open("inputs/input8.txt", "r") as input:
        lines = [line.rstrip() for line in input.readlines()]
    
    codeTotal = 0
    encodeTotal = 0
    
    for line in lines:
        modLine = line[1:-1]
        encode = ""
        for c in modLine:
            if c == "\\":
                encode += ("\\\\")
            elif c == "\"":
                encode += ("\\\"")
            else:
                encode += c

        codeTotal += len(line)
        encodeTotal += (len(encode) + 4 + 2)

    print(f"Part 2: {encodeTotal - codeTotal}")


part1()
part2()
