# In addition to horizontal position and depth, you'll also need to track a third value,
# aim, which also starts at 0. The commands also mean something entirely different than you first thought:
#
# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.
# Using this new interpretation of the commands, calculate the horizontal position and depth
# you would have after following the planned course.
# What do you get if you multiply your final horizontal position by your final depth?

position = 0
depth = 0
aim = 0

with open("route.txt") as f:
    for line in f:
        (k, v) = line.split()
        if k == 'forward':
            position = position + int(v)
            depth = depth + (aim * int(v))
        elif k == 'down':
            aim = aim + int(v)
        elif k == 'up':
            aim = aim - int(v)
print(position)
print(depth)
result = position * depth
print(result)