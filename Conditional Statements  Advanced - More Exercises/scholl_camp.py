season = input()
group = input()
students = int(input())
nights = int(input())

sport = ''
total_price = 0

if season == 'Winter':
    if group == 'girls':
        total_price += (9.60 * nights * students)
        sport = 'Gymnastics'
    elif group == 'boys':
        total_price += (9.60 * nights * students)
        sport = 'Judo'
    elif group == 'mixed':
        total_price += (10 * nights * students)
        sport = 'Ski'

elif season == 'Spring':
    if group == 'girls':
        total_price += (7.20 * nights * students)
        sport = 'Athletics'
    elif group == 'boys':
        total_price += (7.20 * nights * students)
        sport = 'Tennis'
    elif group == 'mixed':
        total_price += (9.50 * nights * students)
        sport = 'Cycling'

elif season == 'Summer':
    if group == 'girls':
        total_price += (15 * nights * students)
        sport = 'Volleyball'
    elif group == 'boys':
        total_price += (15 * nights * students)
        sport = 'Football'
    elif group == 'mixed':
        total_price += (20 * nights * students)
        sport = 'Swimming'

if 50 <= students:
    total_price /= 2
elif 20 <= students < 50:
    total_price *= 0.85
elif 10 <= students < 20:
    total_price *= 0.95

print(f'{sport} {total_price:.2f} lv.')
