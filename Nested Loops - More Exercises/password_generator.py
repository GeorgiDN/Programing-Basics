n_number = int(input())
first_n_letters = int(input())

for num in range(1, n_number + 1):
    for num2 in range(1, n_number + 1):
        for num3 in range(97, 97+first_n_letters):
            letter = chr(num3)
            for num4 in range(97, 97+first_n_letters):
                letter2 = chr(num4)
                for num5 in range(1, n_number + 1):
                    if num5 > num2 and num5 > num:
                        print(f"{num}{num2}{letter}{letter2}{num5}", end=' ')
                      
