import re
from collections import defaultdict

rule_reg = re.compile(r"\d+\|\d+")
exec_reg = re.compile(r"(\d+)+")
rule_set = defaultdict(list)

with open("../Inputs/mockin.txt") as riddle_in:
    riddle_in = [line.rstrip("\n") + "" for line in riddle_in.readlines()]
    # print(riddle_in)
    split_index = riddle_in.index('')
    rules = rule_reg.findall(";".join(riddle_in[0:split_index]))
    execs: list[int] = [[int(x) for x in line.strip().split(",")] for line in riddle_in[split_index + 1::]]
    print(f"Rules: {rules}")
    print(f"Execs: {execs}")


def p1():
    create_ruleset()

    valid_execes = []
    for line in execs:
        if not validate_set(line): valid_execes.append(line)
        # print(f"Exec {line} was {"valid" if isValid else "invalid"} ")
    print(f"P1: {sum(v_exec[len(v_exec) // 2] for v_exec in valid_execes)}")


def validate_set(line):
    for i, fact in enumerate(line):
        isViolation = check_ruleset_violation(fact, line[0:i])
        if isViolation:
            break
    return isViolation


def p2():
    create_ruleset()

    invalid_execs = []
    for line in execs:
        if validate_set(line): invalid_execs.append(line)
    # while (notOrdered)
    print(invalid_execs)
    for invalid_exec in invalid_execs:
        # while (True):
            for i, fact in enumerate(invalid_exec):
                p2_check_ruleset_violation(fact, invalid_exec[0:i])


def create_ruleset():
    for i, rule in enumerate(rules):
        rule_i, fact = [int(x) for x in rule.split("|")]
        rule_set[rule_i].append(fact)
    # print(rule_set)


def check_ruleset_violation(fact: int, prev_execs: list) -> bool:
    rules_for_fact = rule_set[fact]
    violation = any(i in rules_for_fact for i in prev_execs)
    return violation


def p2_check_ruleset_violation(fact: int, prev_execs: list) -> bool:
    rules_for_fact = rule_set[fact]





def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



# p1()
p2()
