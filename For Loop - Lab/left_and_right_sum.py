number = int(input())

left_sum = 0
right_sum = 0

for _ in range(number):
    left_number = int(input())
    left_sum += left_number

for _ in range(number):
    right_number = int(input())
    right_sum += right_number

diff = abs(left_sum - right_sum)

if diff == 0:
    print("Yes, sum =", left_sum)
else:
    print("No, diff =", diff)
