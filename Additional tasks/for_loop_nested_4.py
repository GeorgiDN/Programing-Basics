row = 5

for i in range(1, row + 1, 1):
    for j in range(row, i-1, -1):
        print(j, end=' ')

    print()

# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5
