information = {}

while True:
    ticket_count = 0
    command = input()

    if command == 'Finish':
        break

    film = command
    free_places = int(input())

    for _ in range(free_places):
        film_type = input()

        if film_type == 'End':
            break

        ticket_count += 1
        if film_type not in information:
            information[film_type] = 1
        else:
            information[film_type] += 1

    percent_full = (ticket_count / free_places) * 100
    print(f"{film} - {percent_full:.2f}% full.")


tickets = list(information.values())
tickets_number = sum(tickets)



student_tickets_percent = (information.get("student", 0) / tickets_number) * 100
standard_tickets_percent = (information.get("standard", 0) / tickets_number) * 100
kids_tickets_percent = (information.get("kid", 0) / tickets_number) * 100

print(f"Total tickets: {tickets_number}")
print(f"{student_tickets_percent:.2f}% student tickets.\n"
      f"{standard_tickets_percent:.2f}% standard tickets.\n"
      f"{kids_tickets_percent:.2f}% kids tickets.")
