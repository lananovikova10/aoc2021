# After following these instructions, you would have a horizontal position of
# 15 and a depth of 10. (Multiplying these together produces 150.)
#
# Calculate the horizontal position and depth you would have
# after following the planned course. What do you get if you multiply your final
# horizontal position by your final depth?

position = 0
depth = 0

with open("route.txt") as f:
    for line in f:
        (k, v) = line.split()
        if k == 'forward':
            position = position + int(v)
        elif k == 'down':
            depth = depth + int(v)
        elif k == 'up':
            depth = depth - int(v)
print(position)
print(depth)
result = position * depth
print(result)

