import math
x_sqr_m_vineyard = int(input())
y_grapes_per_sqr_m = float(input())
z_wine_needed_liters = int(input())
workers_number = int(input())

total_grapes = x_sqr_m_vineyard * y_grapes_per_sqr_m
wine = total_grapes * 0.40 / 2.5

diff = abs(wine - z_wine_needed_liters)

if wine >= z_wine_needed_liters:
    distribution = diff / workers_number
    print(f'Good harvest this year! Total wine: {math.floor(wine)} liters.')
    print(f'{math.ceil(diff)} liters left -> {math.ceil(distribution)} liters per person.')
else:
    print(f'It will be a tough winter! More {math.floor(diff)} liters wine needed.')
