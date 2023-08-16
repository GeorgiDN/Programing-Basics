count_pairs = int(input())
pair = 0
lists = []
Flag = True
max_diff_list = []

for i in range(count_pairs):
    num1 = int(input())
    num2 = int(input())
    pair = num1 + num2
    lists.append(pair)

max_value = max(lists)
for p in lists:
    if p != max_value:
        Flag = False
        diff = lists[-1] - lists[-2]
        max_diff_list.append(diff)

if Flag:
    print(f'Yes, value={max_value}')
else:
    max_d = max(max_diff_list)
    print(f'No, maxdiff={abs(max_d)}')
  
