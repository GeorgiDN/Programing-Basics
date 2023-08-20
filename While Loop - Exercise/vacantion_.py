needed_money = float(input())
owned_money = float(input())


days_counter = 0
days_spending_money = 0

while True:
    days_counter += 1
    command = input()
    curr_money = float(input())

    if command == 'spend':
        days_spending_money += 1
        owned_money -= curr_money
        if owned_money <= 0:
            owned_money = 0
    elif command == 'save':
        owned_money += curr_money
        days_spending_money = 0

    if owned_money >= needed_money:
        print(f'You saved the money for {days_counter} days.')
        break
    elif days_spending_money == 5:
        print("You can't save the money.")
        print(days_counter)
        break
