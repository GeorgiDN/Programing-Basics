upper_limit_1 = int(input())
upper_limit_2 = int(input())
upper_limit_3 = int(input())

for digit_1 in range(2, upper_limit_1 + 1, 2):
    for digit_2 in range(2, upper_limit_2 + 1):
        if digit_2 == 2 or digit_2 == 3 or digit_2 == 5 or digit_2 == 7:
            for digit_3 in range(2, upper_limit_3 + 1, 2):
                print(f"{digit_1} {digit_2} {digit_3}")
