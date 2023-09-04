n = int(input())

print('+' + ' ' + (('-' + ' ') * (n-2) + '+'))
for num in range(n-2):
    print('|' + ' ' + (('-' + ' ') * (n-2) + '|'))
print('+' + ' ' + (('-' + ' ') * (n-2) + '+'))
