def even_powers_of_2(n, power=0):
    if power > n / 2:
        return
    else:
        print(2 ** power)
        even_powers_of_2(n, power + 2)


n = int(input())

even_powers_of_2(2 * n)


# number = int(input())

# for num in range(number + 1):
#     if num % 2 == 0:
#         print(2 ** num)
