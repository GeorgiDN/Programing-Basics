is_prime = True
prime_sum = 0
non_prime_sum =0

input_line = input()
while input_line != 'stop':
    curr_num = int(input_line)
    if curr_num < 0:
        print('Number is negative.')
    else:
        for i in range(2, curr_num):
            if curr_num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_sum += curr_num
        else:
            non_prime_sum += curr_num
            is_prime = True

    input_line = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
