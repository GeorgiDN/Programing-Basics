text = input()

vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

total_sum = 0

for char in text:
    if char in vowels:
        total_sum += vowels[char]

print(total_sum)
