start_interval = int(input())
end_interval = int(input())

output = ""

for digit_1 in range(start_interval, end_interval + 1):
    for digit_2 in range(start_interval, end_interval + 1):
        for digit_3 in range(start_interval, end_interval + 1):
            for digit_4 in range(start_interval, end_interval + 1):
                if (digit_1 % 2 == 0 and digit_4 % 2 != 0) or (digit_1 % 2 != 0 and digit_4 % 2 == 0):
                    if digit_1 > digit_4 and (digit_2 + digit_3) % 2 == 0:
                        output += f"{digit_1}{digit_2}{digit_3}{digit_4} "

print(output)
