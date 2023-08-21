cake_length = int(input())
cake_wide = int(input())

cake_peaces = cake_length * cake_wide

while cake_peaces > 0:
    command = input()
    if command == 'STOP':
        print(f"{cake_peaces} pieces are left.")
        break

    cake_peaces -= int(command)

if cake_peaces <= 0:
    print(f"No more cake left! You need {abs(cake_peaces)} pieces more.")
