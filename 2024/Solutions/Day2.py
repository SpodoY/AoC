import re

with open("../Inputs/Day2.txt") as riddle_in:
    riddle_in = [[int(x) for x in line.rstrip("\n").split(" ")] for line in riddle_in.readlines()]

def good(d, s=0):
    for i in range(len(d) - 1):
        if not 1 <= d[i] - d[i + 1] <= 3:
            return s and any(good(d[j - 1:j] + d[j + 1:]) for j in (i, i + 1))
    return True

for s in 0, 1: print(sum(good(d, s) or good(d[::-1], s) for d in riddle_in))
