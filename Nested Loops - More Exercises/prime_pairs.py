import math

start_first = int(input())
start_second = int(input())
end_diff_first = int(input())
end_diff_second = int(input())

final_first = start_first + end_diff_first
final_second = start_second + end_diff_second

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt_num = int(math.sqrt(num)) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False
    return True

for i in range(start_first, final_first + 1):
    for j in range(start_second, final_second + 1):
        if is_prime(i) and is_prime(j):
            print(f'{i}{j}')
          
