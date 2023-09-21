capacity = int(input())
cinema_income = 0
full_condition = False
while True:
    command = input()
    if command == 'Movie time!':
        break

    people = int(command)
    if capacity >= people:
        capacity -= people
        curr_price = people * 5
        cinema_income += curr_price
        if people % 3 == 0:
            curr_price -= 5
            cinema_income -= 5
    else:
        full_condition = True
        break

if full_condition:
    print(f"The cinema is full.\n"
          f"Cinema income - {cinema_income} lv.")
else:
    print(f"There are {capacity} seats left in the cinema.\n"
          f"Cinema income - {cinema_income} lv.")
