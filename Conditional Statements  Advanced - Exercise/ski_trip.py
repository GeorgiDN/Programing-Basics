day_stay_num = int(input())
room = input()
assessment = input()

price = 0

if room == 'room for one person':
    price = 18 * (day_stay_num - 1)
elif room == 'apartment':
    if day_stay_num < 10:
        price = 25 * (day_stay_num - 1) * 0.70
    elif 10 <= day_stay_num <= 15:
        price = 25 * (day_stay_num - 1) * 0.65
    elif day_stay_num > 15:
        price = 25 * (day_stay_num - 1) * 0.5
elif room == 'president apartment':
    if day_stay_num < 10:
        price = 35 * (day_stay_num - 1) * 0.90
    elif 10 <= day_stay_num <= 15:
        price = 35 * (day_stay_num - 1) * 0.85
    elif day_stay_num > 15:
        price = 35 * (day_stay_num - 1) * 0.80
if assessment == 'positive':
    price += (price * 0.25)
elif assessment == 'negative':
    price -= (price * 0.10)

print(f'{price:.2f}')
