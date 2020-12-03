with open('input.txt') as f:
    lines = f.read().strip().splitlines()
    for line in lines:
        i = 0
        # print(f"testing line {line}")
        while i < len(lines):
            z = 0
            # print(f"testing with i {lines[i]}")
            while z < len(lines):
                # print(f"testing with z {lines[z]}")
                if int(line) + int(lines[i]) + int(lines[z]) == 2020:
                    product = int(line) * int(lines[i]) * int(lines[z])
                    print(f"{line} * {lines[i]} * {lines[z]} = {product}")
                z += 1
            i += 1
