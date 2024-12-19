import re

with open("../Inputs/Day3.txt") as riddle_in:
    riddle_in = "".join([line.rstrip("\n") for line in riddle_in.readlines()])

valid_expression_p1 = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)", re.IGNORECASE)
valid_expression_p2 = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\)|do\(\))", re.IGNORECASE)


def p1():
    matches = valid_expression_p1.findall(riddle_in)
    print(f"P1: {sum([int(m[0]) * int(m[1]) for m in matches])}")


def p2():
    matches = valid_expression_p2.findall(riddle_in)
    result = 0
    cur_blocked = False
    for match in matches:
        if match[2] != '':
            cur_blocked = match[2] == "don't()"
            continue
        if not cur_blocked: result += int(match[0]) * int(match[1])
    print(f"P2: {result}")


p1()
p2()
