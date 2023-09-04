n = int(input())

# Горна част на ромба
for row in range(1, n + 1):
    spaces = " " * (n - row)
    stars = "* " * row
    print(f"{spaces}{stars}")

# Долна част на ромба
for row in range(n - 1, 0, -1):
    spaces = " " * (n - row)
    stars = "* " * row
    print(f"{spaces}{stars}")
