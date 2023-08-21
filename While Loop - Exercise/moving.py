wide_free_space = int(input())
length_free_space = int(input())
high_free_space = int(input())

total_free_space = wide_free_space * length_free_space * high_free_space
cartons_count = 0
has_finished = True

while total_free_space > cartons_count:
    command = input()
    if command == 'Done':
        has_finished = False
        break
    curr_carton = int(command)
    cartons_count += curr_carton

if has_finished:
    print(f'No more free space! You need {abs(total_free_space - cartons_count)} Cubic meters more.')
else:
    print(f'{total_free_space - cartons_count} Cubic meters left.')
