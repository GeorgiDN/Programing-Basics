a = int(input())
b = int(input())
max_num_passwords = int(input())

count_combinations = 0

first_char = 35
i1 = chr(first_char)

sec_char = 64
i2 = chr(sec_char)

for i3 in range(1, a + 1):
    for i4 in range(1, b + 1):
        password = f"{i1}{i2}{i3}{i4}{i2}{i1}"
        print(password, end='|')
        first_char += 1
        if first_char > 55:
            first_char = 35
        sec_char += 1
        if sec_char > 96:
            sec_char = 64
        i1 = chr(first_char)
        i2 = chr(sec_char)
        count_combinations += 1
        if count_combinations >= max_num_passwords:
            break
    if count_combinations >= max_num_passwords:
        break
      
