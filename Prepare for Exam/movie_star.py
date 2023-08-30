budget = float(input())
command = input()

renumeration = 0

while command != 'ACTION':
    if (len(command)) <= 15:
        renumeration = float(input())
        budget -= renumeration
    elif(len(command)) > 15:
        renumeration = budget * 0.20
        budget -= renumeration

    if budget <= 0:
        break
    command = input()

if budget <= 0:
    print(f"We need {abs(budget):.2f} leva for our actors.")
else:
    print(f"We are left with {abs(budget):.2f} leva.")
