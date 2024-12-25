import itertools
import time

from utils.Utils import read_file

riddle_in = read_file("../Inputs/Day7.txt")
riddle_in = [(int(line.split(":")[0]), list(map(int, line.split(":")[1].split()))) for line in riddle_in]


def evaluate_expression(inputs, ops):
    result = inputs[0]
    for i, num in enumerate(inputs):
        if i == 0: continue
        if ops[i - 1] == "||":
            result = int(str(result) + str(inputs[i]))
        elif ops[i - 1] == "*":
            result *= inputs[i]
        else:
            result += inputs[i]
    return result


def calc_result(operations):
    valid_results = []
    for riddle in riddle_in:
        result, inputs = riddle
        ops_count = len(inputs) - 1

        all_ops_permutations = [list(p) for p in list(itertools.product(operations, repeat=ops_count))]

        for ops in all_ops_permutations:
            # print(f"{inputs}|{ops}: {evaluate_expression(inputs, ops)}")
            if result == evaluate_expression(inputs, ops):
                valid_results.append(result)
                break

    print(valid_results)
    print(f"P1: {sum(valid_results)}")


start = time.time()
calc_result(("*", "+"))
print(f"P1 runtime: {time.time() - start} seconds")

start = time.time()
calc_result(("*", "+", "||")) # Runs for about 45 Seconds on my laptop - No time to make it efficient rn
print(f"P2 runtime: {time.time() - start} seconds")
