n = int(input())
roof_rows = (n + 1) // 2

for row in range(roof_rows):
    if row == 0:
        if n % 2 == 0:
            print("-" * ((n // 2) - 1) + "**" + "-" * ((n // 2) - 1))
        elif n % 2 != 0:
            print("-" * int(((n + 1) // 2) - 1) + "*" + "-" * int(((n + 1) // 2) - 1))
    else:
        if n % 2 == 0:
            print("-" * (((n // 2) - 1) - row) + "*" + "*" * (2 * row + 1) + "-" * (((n // 2) - 1) - row))
        elif n % 2 != 0:
            print("-" * (((n + 1) // 2) - row - 1) + "*" + "*" * (2 * row) + "-" * (((n + 1) // 2) - row - 1))


base_rows = (n // 2) - 1
for base_row in range(base_rows + 1):
    print("|" + "*" * (n - 2) + "|")
