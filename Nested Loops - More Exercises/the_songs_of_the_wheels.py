control_value = int(input())
digit_counter = 0

a = 0
b = 0
c = 0
d = 0

for digit_1 in range(1, 10):
    for digit_2 in range(1, 10):
        for digit_3 in range(1, 10):
            for digit_4 in range(1, 10):
                if digit_1 < digit_2 and digit_3 > digit_4 and (digit_1 * digit_2) + (digit_3 * digit_4) == \
                        control_value:
                    number = f'{digit_1}{digit_2}{digit_3}{digit_4}'
                    print(number, end=' ')
                    digit_counter += 1
                    if digit_counter == 4:
                        a = digit_1
                        b = digit_2
                        c = digit_3
                        d = digit_4

if digit_counter >= 4:
    print()
    print(f'Password: {a}{b}{c}{d}')
elif digit_counter < 4:
    print('No!')
  
