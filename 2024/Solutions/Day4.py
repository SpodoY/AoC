with open("../Inputs/Day4.txt") as riddle_in:
    riddle_in = [line.rstrip("\n") for line in riddle_in.readlines()]

check_word = "XMAS"


def count_occurrences(x, y, dx, dy, word):
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if not (0 <= nx < len(riddle_in) and 0 <= ny < len(riddle_in[0]) and riddle_in[nx][ny] == word[i]):
            return 0
    return 1


def count_word_in_grid(word):
    directions = [
        (0, 1),  # r
        (1, 0),  # d
        (1, 1),  # dr
        (1, -1),  # dl
        (0, -1),  # l
        (-1, 0),  # u
        (-1, -1),  # ul
        (-1, 1)  # ur
    ]
    count = 0

    for x in range(len(riddle_in)):
        for y in range(len(riddle_in[0])):
            for dx, dy in directions:
                count += count_occurrences(x, y, dx, dy, word)

    return count


def p1():
    print(f"P1: {count_word_in_grid(check_word)}")


def p2():
    count = 0

    for x in range(1, len(riddle_in) - 1):
        for y in range(1, len(riddle_in[0]) - 1):
            block = [riddle_in[x - 1][(y - 1):(y + 2)], riddle_in[x][y - 1:y + 2], riddle_in[x + 1][y - 1:y + 2]]
            l, r = '', ''
            for i in range(3):
                l += block[i][i]
                r += block[i][2 - i]
            if ((l == "MAS" and r == "SAM")
                    or (r == "MAS" and l == "SAM")
                    or (l == "SAM" and r == "SAM")
                    or (l == "MAS" and r == "MAS")):
                print(block, x, y)
                count += 1
    print(f"P2: {count}")


p1()
p2()
