start_char = input()
end_char = input()
skip_char = input()

count = 0

for char_1 in range(ord(start_char), ord(end_char) + 1):
    if chr(char_1) == skip_char:
        continue

    for char_2 in range(ord(start_char), ord(end_char) + 1):
        if chr(char_2) == skip_char:
            continue

        for char_3 in range(ord(start_char), ord(end_char) + 1):
            if chr(char_3) == skip_char:
                continue

            combination = chr(char_1) + chr(char_2) + chr(char_3)
            print(combination, end=' ')
            count += 1

print(count, end='')
