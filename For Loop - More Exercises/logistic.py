load_num = int(input())

total_tons = 0
bus = 0
truck = 0
train = 0
total_sum = 0

for i in range(load_num):
    load_tons = int(input())
    if load_tons <= 3:
        bus += load_tons
        total_sum += load_tons * 200
        total_tons += load_tons
    elif 4 <= load_tons <= 11:
        truck += load_tons
        total_sum += load_tons * 175
        total_tons += load_tons
    elif 12 <= load_tons:
        train += load_tons
        total_sum += load_tons * 120
        total_tons += load_tons

average_price_ton = total_sum / total_tons
percent_bus = bus / total_tons * 100
percent_truck = truck / total_tons * 100
percent_train = train / total_tons * 100

print(f'{average_price_ton:.2f}')
print(f'{percent_bus:.2f}%')
print(f'{percent_truck:.2f}%')
print(f'{percent_train:.2f}%')
