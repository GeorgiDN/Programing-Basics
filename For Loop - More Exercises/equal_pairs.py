n = int(input())

values = []

for i in range(n):
    curr_first_num = int(input())
    curr_sec_num = int(input())
    total_first_and_sec_num = curr_first_num + curr_sec_num
    values.append(total_first_and_sec_num)

if len(set(values)) == 1:
    print(f"Yes, value={values[0]}")
else:
    max_diff = max(abs(values[i] - values[i+1]) for i in range(len(values)-1))
    print(f"No, maxdiff={max_diff}")
    
