import re

with open("../inputs/Day1.txt") as riddle_in:
    riddle_in = [re.split(r" +", line.rstrip("\n")) for line in riddle_in.readlines()]

l_list = [int(x[0]) for x in riddle_in]
r_list = [int(x[1]) for x in riddle_in]
l_list.sort()
r_list.sort()

def p1():
    diffs = [abs(l_list[i] - r_list[i]) for i in range(len(l_list))]
    print(f"Sol: {sum(diffs)}")


def p2():
    ans = 0
    occs = dict()
    for i in range(len(l_list)):
        if l_list[i] not in occs:
            occs[l_list[i]] = r_list.count(l_list[i]) * l_list[i]
        ans += occs[l_list[i]]
    print(f"Sol p2: {ans}")


p1()
p2()
