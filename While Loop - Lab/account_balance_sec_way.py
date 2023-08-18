account_balance = 0

while True:
    command = input()

    if command == 'NoMoreMoney':
        break

    curr_sum = float(command)

    if curr_sum >= 0:
        account_balance += curr_sum
        print(f"Increase: {curr_sum:.2f}")
    else:
        print('Invalid operation!')
        break

print(f'Total: {account_balance:.2f}')
