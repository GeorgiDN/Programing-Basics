#https://judge.softuni.org/Contests/Practice/DownloadResource/5526

voucher = int(input())
no_money = False

ticket_count = 0
product_count = 0

while True:
    if no_money:
        break

    command = input()

    if command == 'End':
        break

    else:
        purchase = command

        if len(purchase) > 8:
            film_ticket_price = ord(purchase[0]) + ord(purchase[1])

            if film_ticket_price <= voucher:
                voucher -= film_ticket_price
                ticket_count += 1
            else:
                no_money = True
                break

        elif len(purchase) <= 8:
            product_price = ord(purchase[0])

            if product_price <= voucher:
                voucher -= product_price
                product_count += 1
            else:
                no_money = True
                break

print(ticket_count)
print(product_count)
