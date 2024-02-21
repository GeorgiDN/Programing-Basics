def recursion_numbers(start_num_):
    if start_num_ > final_num:
        return
    else:
        print(start_num_)
        recursion_numbers(start_num_ + 3)


final_num = int(input())
start_num = (final_num - final_num) + 1
recursion_numbers(start_num)



# Basic
# n = int(input())
# for num in range(1, n + 1, 3):
#     print(num)
