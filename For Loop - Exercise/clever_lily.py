age = int(input())
laundry_price = float(input())
toy_price = int(input())

money = 0
toys_number = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money += i * 5
        money -= 1
    elif i % 2 != 0:
        toys_number += 1

sum_sold_toys = toys_number * toy_price
total_sum = money + sum_sold_toys

diff = abs(total_sum - laundry_price)

if total_sum >= laundry_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
