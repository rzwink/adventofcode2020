from math import ceil


def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length / len(string_to_expand)) + 1))[:length]


def expand_map(lines, x, y):
    max_width = x * y * len(lines)
    max_multiplier = ceil(max_width / len(lines[0]))

    i = 0
    while i < len(lines):
        lines[i] = max_multiplier * lines[i]
        i += 1

    return lines


def count_trees(lines, x, y):
    orig_x = x
    orig_y = y
    trees = 0

    while y < len(lines):
        if x >= len(lines[y]):
            x = x - len(lines[y])

        if lines[y][x] == '#':
            trees += 1

        x += orig_x
        y += orig_y

    return trees


with open('input.txt') as f:
    input = f.read().strip().splitlines()

    one = count_trees(input, 1, 1)

    two = count_trees(input, 3, 1)

    three = count_trees(input, 5, 1)

    four = count_trees(input, 7, 1)

    five = count_trees(input, 1, 2)

    print(f"{one} {two} {three} {four} {five} = {one * two * three * four * five}")
