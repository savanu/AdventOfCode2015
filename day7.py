import re
from enum import Enum
from collections.abc import Mapping

assignInstr = re.compile('([0-9a-z]+) -> ([a-z]+)')
notInstr = re.compile('NOT ([a-z]+) -> ([a-z]+)')
instr = re.compile('([a-z0-9]+) (AND|OR|RSHIFT|LSHIFT) ([a-z0-9]+) -> ([a-z]+)')

class Wire:

    def __init__(self, name: str, lOperand, rOperand, oper: str, val: int):
        self.lOperand: str = lOperand
        self.rOperand: str = rOperand
        self.oper: str = oper
        self.name: str = name
        self.val: int = val
    
    @staticmethod
    def assign(name: str, lOperand: str):
        return Wire(name, lOperand, None, 'ASSIGN', None)
    
    @staticmethod
    def notInstr(name: str, rOperand: str):
        return Wire(name, None, rOperand, 'NOT', None)
    
    @staticmethod
    def instr(name: str, lOperand, rOperand, oper: str):
        return Wire(name, lOperand, rOperand, oper, None)
    
    def __repr__(self) -> str:
        if self.oper == 'ASSIGN':
            return f"{self.val} -> {self.name}"
        elif self.oper == 'NOT':
            return f"NOT {self.rOperand} -> {self.name}"
        else:
            return f"{self.lOperand} {self.oper} {self.rOperand} -> {self.name}"
    
def loadInput():
    with open('inputs/input7.txt', 'r') as input:
        lines = [x.rstrip() for x in input.readlines()]

    wires = {}

    for line in lines:
        if match := assignInstr.match(line):
            lOperand, name = match.groups()
            wires[name] = Wire.assign(name, lOperand)
        elif match := notInstr.match(line):
            rOperand, name = match.groups()
            wires[name] = Wire.notInstr(name, rOperand)
        elif match := instr.match(line):
            lOperand, oper, rOperand, name = match.groups()
            wires[name] = Wire.instr(name, lOperand, rOperand, oper)
    
    return wires

def part1():
    wires = loadInput()
    resolve(wires, "a")
    
    print(f'Part 1. Wire a: {wires["a"].val}')

def part2():
    wires = loadInput()
    wires["b"] = Wire.assign("b", "3176")

    resolve(wires, "a")

    print(f'Part 2. Wire a: {wires["a"].val}')


def resolve(wires: Mapping[str, Wire], name: str):
    if name.isdigit():
        return int(name)
    
    wire = wires[name]
    if wire.val is not None:
        return wire.val
    
    if wire.oper == 'ASSIGN':
        wire.val = resolve(wires, wire.lOperand)
    elif wire.oper == 'NOT':
        wire.val = (~resolve(wires, wire.rOperand)) & 0xffff
    elif wire.oper == 'LSHIFT':
        wire.val = (resolve(wires, wire.lOperand) << resolve(wires, wire.rOperand)) & 0xffff
    elif wire.oper == 'RSHIFT':
        wire.val = (resolve(wires, wire.lOperand) >> resolve(wires, wire.rOperand)) & 0xffff
    elif wire.oper == 'AND':
        wire.val = (resolve(wires, wire.lOperand) & resolve(wires, wire.rOperand)) & 0xffff
    elif wire.oper == 'OR':
        wire.val = (resolve(wires, wire.lOperand) | resolve(wires, wire.rOperand)) & 0xffff

    return wire.val

part1()
part2()