filename = "day01/input"

with open(filename) as file_object:
    lines = list(map(lambda x: int(x), file_object.readlines()))


# Part 1
prev = lines[0]

increase = 0

for line in lines:
    if line > prev:
        increase = increase + 1

    prev = line

print(increase)


# Part 2

window_size = 3
increase = 0

import math

prev = math.inf

for line in range(0, len(lines) - (window_size - 1)):
    curr = 0
    for i in range(0, 3):
        curr = curr + lines[line + i]
    
    if curr > prev:
        increase = increase + 1
    
    prev = curr

print(increase)