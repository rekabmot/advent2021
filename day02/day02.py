filename = "day02/input"

with open(filename) as file_object:
    instructions = list(map(lambda x: x.split(), file_object.readlines()))

operations = {
    'forward': lambda position, delta: (position[0] + delta, position[1] + (delta * position[2]), position[2]),
    'down': lambda position, delta: (position[0], position[1], position[2] + delta),
    'up': lambda position, delta: (position[0], position[1], position[2] - delta)
}

position = (0, 0, 0)

for instruction in instructions:
    position = operations[instruction[0]](position, int(instruction[1]))

print(position[0] * position[1])