destination = input()
minimal_budged = float(input())
saved_money = 0


while destination != 'End':

    while saved_money < minimal_budged:

        curr_money = float(input())
        saved_money += curr_money

    print(f"Going to {destination}!")
    saved_money = 0
    destination = input()
    if destination == 'End':
        break
    minimal_budged = float(input())
