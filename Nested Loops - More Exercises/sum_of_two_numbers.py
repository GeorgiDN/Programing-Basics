starting_interval = int(input())
final_interval = int(input())
magic_number = int(input())

combination_counter = 0
output = ''
x = 0
y = 0

for x in range(starting_interval, final_interval + 1):
    for y in range(starting_interval, final_interval + 1):

        combination_counter += 1
        if x + y == magic_number:
            output = f"Combination N:{combination_counter} ({x} + {y} = {magic_number})"
            break

    if x + y == magic_number:
        print(output)
        break
if x + y != magic_number:
    output = f"{combination_counter} combinations - neither equals {magic_number}"
    print(output)
