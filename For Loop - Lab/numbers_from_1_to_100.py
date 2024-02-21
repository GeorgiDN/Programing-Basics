def recursion_numbers(n):
    if n > 100:
        return n
    else:
        print(n)
        return recursion_numbers(n + 1)


num = 1
recursion_numbers(num)



# Basic
for number in range(1, 101):
    print(number)
    
