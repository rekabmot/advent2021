filename = "day03/input"

with open(filename) as file_object:
    lines = list(map(lambda x: [int(y) for y in x.strip()], file_object.readlines()))



number_of_lines = len(lines)


def get_totals_by_position(lines):
    totals_by_position = [0] * len(lines[0])

    for line in lines:
        for i in range(0, len(line)):
            if line[i] == 1:
                totals_by_position[i] += 1
    
    return totals_by_position


gamma = []
epsilon = []


for total in get_totals_by_position(lines):
    if total > number_of_lines / 2:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

print(int(''.join(map(lambda x: str(x), gamma)), base=2) * int(''.join(map(lambda x: str(x), epsilon)), base=2))

oxygen = lines.copy()
co2 = lines.copy()


def derive_gas_value(gas, comparison):
    for i in range(0, len(gas[0])):
        gas_totals_by_position = get_totals_by_position(gas)

        if comparison(gas_totals_by_position, gas, i):
            match_value = 1
        else:
            match_value = 0

        gas = list(filter(lambda x: x[i] == match_value, gas))

        if len(gas) == 1:
            return int(''.join(map(lambda x: str(x), gas[0])), base=2)

x = derive_gas_value(oxygen, lambda x, y, i: x[i] >= len(y) - x[i])
y = derive_gas_value(co2, lambda x, y, i: x[i] < len(y) - x[i])

print(x * y)




# for i in range(0, len(lines[0])):
#     oxygen_totals_by_position = get_totals_by_position(oxygen)
#     co2_totals_by_position = get_totals_by_position(co2)

#     if oxygen_totals_by_position[i] >= len(oxygen) - oxygen_totals_by_position[i]:
#         oxygen_match_value = 1
#     else:
#         oxygen_match_value = 0

#     if co2_totals_by_position[i] < len(co2) - co2_totals_by_position[i]:
#         co2_match_value = 1
#     else:
#         co2_match_value = 0

#     oxygen = list(filter(lambda x: x[i] == oxygen_match_value, oxygen))
#     co2 = list(filter(lambda x: x[i] == co2_match_value, co2))
#     print(co2)

# print(oxygen)
# print(co2)
        
