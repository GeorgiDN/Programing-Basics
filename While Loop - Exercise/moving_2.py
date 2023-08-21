wide_free_space = int(input())
length_free_space = int(input())
high_free_space = int(input())

space_volume = wide_free_space * length_free_space * high_free_space

while space_volume > 0:
    command = input()
    if command == 'Done':
        break

    space_volume -= int(command)

if space_volume > 0:
    print(f'{space_volume} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(space_volume)} Cubic meters more.')
