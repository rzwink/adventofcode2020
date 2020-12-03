def has_num_times(s, c, min, max):
    i = 0
    found = 0
    while i < len(s):
        if s[i] == c:
            found += 1
        i += 1
    return int(min) <= found <= int(max)


def has_num_places(s, c, p1, p2):
    p1 = int(p1) - 1
    p2 = int(p2) - 1

    if len(s) <= p1:
        return False
    elif len(s) < p2:

        return s[p1] == c
    else:

        if s[p1] == c and s[p2] != c:
            return True
        elif s[p1] != c and s[p2] == c:
            return True
        else:
            return False


with open('input.txt') as f:
    lines = f.read().strip().splitlines()
    valid = 0
    for line in lines:
        parts = line.split(":")

        pattern = parts[0].split(" ")[1]
        length = parts[0].split(" ")[0]

        result = has_num_places(parts[1].strip(), pattern, length.split("-")[0], length.split("-")[1])

        if result:
            valid += 1

    print(valid)
