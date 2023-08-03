screening_type = input()
rows = int(input())
columns = int(input())

tickets = rows * columns
income = 0

if screening_type == 'Premiere':
    income += tickets * 12
elif screening_type == 'Normal':
    income += tickets * 7.50
elif screening_type == 'Discount':
    income += tickets * 5.00

print(f'{income:.2f}')
