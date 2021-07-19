import re

doubleletter = re.compile('([a-z])\\1')
restricted = re.compile('(ab)+|(cd)+|(pq)+|(xy)+')

twoLettersTwice = re.compile('([a-z][a-z])[a-z]*\\1')
letterRepeatBetween = re.compile('([a-z])[a-z]{1}\\1')

def part1():
    with open('inputs/input5.txt', 'r') as input:
        words = input.readlines()
    
    nicewords = [word for word in words if nice1(word)]

    print(len(nicewords))

def nice1(word: str):
    rule1 = restricted.search(word)
    rule2 = doubleletter.search(word)
    rule3 = len([c for c in word if c in 'aeiou']) >= 3

    return (not rule1) and rule2 and rule3

def nice2(word):
    rule1 = twoLettersTwice.search(word)
    rule2 = letterRepeatBetween.search(word)

    return rule1 and rule2

def part2():
    with open('inputs/input5.txt', 'r') as input:
        words = input.readlines()
    
    niceWords = [word for word in words if nice2(word)]

    print(len(niceWords))
    

part1()
part2()