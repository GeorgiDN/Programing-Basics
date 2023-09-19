
information = {}

while True:
    film = input()
    if film == 'Finish':
        break

    free_seats = int(input())
    ticket_count = 0

    for _ in range(free_seats):
        ticket_type = input()
        if ticket_type == 'End':
            break

        ticket_count += 1
        if ticket_type not in information:
            information[ticket_type] = 1
        else:
            information[ticket_type] += 1

    percent_full = (ticket_count / free_seats) * 100
    print(f"{film} - {percent_full:.2f}% full.")

tickets = list(information.values())
tickets_number = sum(tickets)

student_tickets_percent = (information.get("student", 0) / tickets_number) * 100
standard_tickets_percent = (information.get("standard", 0) / tickets_number) * 100
kids_tickets_percent = (information.get("kid", 0) / tickets_number) * 100

print(f"Total tickets: {tickets_number}")
print(f"{student_tickets_percent:.2f}% student tickets.")
print(f"{standard_tickets_percent:.2f}% standard tickets.")
print(f"{kids_tickets_percent:.2f}% kids tickets.")
