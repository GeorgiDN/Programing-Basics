def sum_numbers(n):
    if n == 0:
        return 0
    else:
        num = int(input())
        return num + sum_numbers(n - 1)


n = int(input())
print(sum_numbers(n))



###############################################
# def sum_numbers(nums, idx=0):
#     if idx == len(nums):
#         return 0
#     else:
#         return nums[idx] + sum_numbers(nums, idx + 1)
#
#
# n = int(input())
# nums = [int(input()) for _ in range(n)]
#
# sum_numbers(nums)
# print(sum_numbers(nums))



###############################################
# n = int(input())
# nums = [int(input()) for x in range(n)]
# print(sum(nums))



###############################################
# number = int(input())
#
# total_sum = 0
#
# for _ in range(number):
#     current_number = int(input())
#     total_sum += current_number
#
# print(total_sum)
