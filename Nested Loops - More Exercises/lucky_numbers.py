n = int(input())

output = ""

for digit_1 in range(1, 10):
    for digit_2 in range(1, 10):
        for digit_3 in range(1, 10):
            for digit_4 in range(1, 10):
                if digit_1 + digit_2 == digit_3 + digit_4 and n % (digit_1 + digit_2) == 0:
                    output += f"{digit_1}{digit_2}{digit_3}{digit_4} "

print(output)
