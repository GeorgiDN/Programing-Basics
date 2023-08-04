flowers = input()
num_flowers = int(input())
budget = int(input())
price = 0

if flowers == 'Roses':
    if num_flowers > 80:
        price = 5 * num_flowers * 0.90
    else:
        price = 5 * num_flowers
elif flowers == 'Dahlias':
    if num_flowers > 90:
        price = 3.80 * num_flowers * 0.85
    else:
        price = 3.80 * num_flowers
elif flowers == 'Tulips':
    if num_flowers > 80:
        price = 2.80 * num_flowers * 0.85
    else:
        price = 2.80 * num_flowers
elif flowers == 'Narcissus':
    if num_flowers < 120:
        price = 3 * num_flowers * 1.15
    else:
        price = 3 * num_flowers
elif flowers == 'Gladiolus':
    if num_flowers < 80:
        price = 2.50 * num_flowers * 1.20
    else:
        price = 2.50 * num_flowers

diff = abs(price - budget)
if budget >= price:
    print(f'Hey, you have a great garden with {num_flowers} {flowers} and {diff:.2f} leva left.')
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
