film = input()
free_seats = int(input())

ticket_type = ''

student_ticket_count_total = 0
standard_ticket_count_total = 0
kid_ticket_count_total = 0

student_ticket_count = 0
standard_ticket_count = 0
kid_ticket_count = 0
sum_ticket_per_film = 0
percent_full = 0

while film != 'Finish':
    for i in range(free_seats):
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == "student":
            student_ticket_count += 1
            student_ticket_count_total += 1
        elif ticket_type == "standard":
            standard_ticket_count += 1
            standard_ticket_count_total += 1
        elif ticket_type == "kid":
            kid_ticket_count += 1
            kid_ticket_count_total += 1

    sum_ticket_per_film = student_ticket_count + standard_ticket_count + kid_ticket_count
    percent_full = sum_ticket_per_film / free_seats * 100

    if sum_ticket_per_film == free_seats:
        print(f"{film} - 100.00% full.")
    else:
        print(f"{film} - {percent_full:.2f}% full.")

    student_ticket_count = 0
    standard_ticket_count = 0
    kid_ticket_count = 0
    sum_ticket_per_film = 0
    

    film = input()
    if film == 'Finish':
        break
    free_seats = int(input())

total_sum_ticket = student_ticket_count_total + standard_ticket_count_total + kid_ticket_count_total
percent_student_ticket = student_ticket_count_total / total_sum_ticket * 100
percent_standard_ticket = standard_ticket_count_total / total_sum_ticket * 100
percent_kid_ticket = kid_ticket_count_total / total_sum_ticket * 100

print(f"Total tickets: {total_sum_ticket}")
print(f"{percent_student_ticket:.2f}% student tickets.")
print(f"{percent_standard_ticket:.2f}% standard tickets.")
print(f"{percent_kid_ticket:.2f}% kids tickets.")
