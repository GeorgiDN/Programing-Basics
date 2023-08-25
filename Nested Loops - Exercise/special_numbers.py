n = int(input())

for i in range(1111, 10000):
    is_special = True
    num_to_str = str(i)
    for j in range(len(num_to_str)):
        curr_num = int(num_to_str[j])
        if curr_num == 0 or n % curr_num != 0:
            is_special = False
            break

    if is_special:
        print(i, end=' ')
