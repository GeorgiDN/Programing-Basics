inherited_money = float(input())
year_living = int(input())

year = 1800
curr_age = 18

rest_money = inherited_money

for i in range(year, year_living + 1):
    if i % 2 == 0:
        rest_money -= 12000
        curr_age += 1
    elif i % 2 != 0:
        rest_money -= 12000 + 50 * curr_age
        curr_age += 1

diff = abs(inherited_money - rest_money)
rest_money = abs(rest_money)

if inherited_money >= diff:
    print(f"Yes! He will live a carefree life and will have {rest_money:.2f} dollars left.")
else:
    print(f"He will need {rest_money:.2f} dollars to survive.")
