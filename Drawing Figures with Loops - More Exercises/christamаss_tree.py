n = int(input())

for i in range(n + 1):
    print(" " * (n - i) + ("*" * i) + " | " + ("*" * i))


# n = int(input())

# for row in range(n+1):
#     spaces = " " * (n - row)
#     stars = "*" * row + ' '
#     space_1 = ' '
#     print(f"{spaces}{stars}|{space_1}{stars}")
