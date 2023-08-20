steps_counter = 0

while steps_counter < 10000:
    command = input()
    if command == 'Going home':
        curr_step = int(input())
        steps_counter += curr_step
        break
    steps_counter += int(command)

if steps_counter >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{abs(steps_counter - 10000)} steps over the goal!')
else:
    print(f'{abs(10000 - steps_counter)} more steps to reach goal.')
