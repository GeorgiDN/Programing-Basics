# With recursion
def numbers_in_reversed(n):
    if n == 0:
        return n
    else:
        print(n)
        return numbers_in_reversed(n - 1)


num = int(input())
numbers_in_reversed(num)


# Basic
# number = int(input())

# for num in range(number, 0, -1):
#     print(num)
