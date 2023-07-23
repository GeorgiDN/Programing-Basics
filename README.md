[Exam-Preparation-March-2021.docx]
(https://github.com/GeorgiDN/Programing-Basics/files/12138372/Exam-Preparation-March-2021.docx)

airline = input()
num_tickets_adult = int(input())
num_tickets_kid = int(input())
price_ticket_adult = float(input())
price_service = float(input())

price_kid_ticket = price_ticket_adult * 0.3

adult_total = (price_ticket_adult + price_service) * num_tickets_adult
kid_total = (price_kid_ticket + price_service) * num_tickets_kid

total_sum = adult_total + kid_total

profit = total_sum * 0.2

print(f"The profit of your agency from {airline} tickets is {profit:.2f} lv.")

