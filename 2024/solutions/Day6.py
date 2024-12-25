import time
from enum import Enum

from utils.Utils import *


class Direction(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)


def is_oob(row, col):
    return not (0 <= col < len(riddle_in[0]) and 0 <= row < len(riddle_in))


def check_collision(row, col):
    if not is_oob(row, col):
        return riddle_in[row][col] == WALL


def index2d(value):
    return next((i, j) for i, lst in enumerate(riddle_in) for j, x in enumerate(lst) if x == value)


def print_grid():
    print("\n".join(riddle_in))


def do_move(row, col):
    global current_dir
    new_pos = [sum(x) for x in zip((row, col), current_dir.value)]
    if check_collision(new_pos[0], new_pos[1]):
        new_dir = dir_list[(list(Direction).index(current_dir) + 1) % len(dir_list)]
        current_dir = new_dir
        new_pos = [sum(x) for x in zip((row, col), current_dir.value)]
    riddle_in[row] = riddle_in[row][0:col] + VISITED + riddle_in[row][col + 1:]
    return new_pos


GUARD = "^"
WALL = "#"
VISITED = "X"
dir_list = list(Direction)
current_dir = Direction.NORTH

riddle_in = read_file("../inputs/mockin.txt")


def p1():
    row, col = index2d(GUARD)
    while not is_oob(row, col):
        row, col = do_move(row, col)

    print_grid()
    print(f"P1: {"\n".join(riddle_in).count(VISITED)}")


def p2():
    start_pos = index2d(GUARD)
    row, col = start_pos
    while not is_oob(row, col):
        row, col = do_move(row, col)
    loop_variants = 0
    print(f"P2: {loop_variants}")


p1()
