budged_group = int(input())
season = input()
fishermans = int(input())

price_rent = 0
discount = 0
sec_discount = 0

if season == 'Spring':
    price_rent = 3000
    if fishermans <= 6:
        discount += 0.1
    elif 7 <= fishermans <= 11:
        discount += 0.15
    elif fishermans >= 12:
        discount += 0.25
elif season == 'Summer' or season == 'Autumn':
    price_rent = 4200
    if fishermans <= 6:
        discount += 0.1
    elif 7 <= fishermans <= 11:
        discount += 0.15
    elif fishermans >= 12:
        discount += 0.25
elif season == 'Winter':
    price_rent = 2600
    if fishermans <= 6:
        discount += 0.1
    elif 7 <= fishermans <= 11:
        discount += 0.15
    elif fishermans >= 12:
        discount += 0.25
if fishermans % 2 == 0 and (season == 'Summer' or season == 'Winter' or season == 'Spring'):
    sec_discount += 0.05

total_price = price_rent * (1 - discount) * (1 - sec_discount)
diff = abs(total_price - budged_group)

if budged_group >= total_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
