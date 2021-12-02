# How many measurements are larger than the previous measurement?

with open('input.txt', 'r', encoding='utf8') as rp:
    lines = []
    for line in rp:
        lines.append(line.rstrip("\n"))
    counter = 0
    for e in range(len(lines) - 1):
        previous = int(lines[e])
        current = int(lines[e + 1])
        if current > previous:
            counter += 1
    print(counter)
    print(e)