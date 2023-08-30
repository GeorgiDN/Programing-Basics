drink_kind = input()
sugar = input()
drinks_num = int(input())

total_price = 0

if drink_kind == "Espresso":
    if sugar == 'Without':
        total_price += (0.9 * drinks_num) * 0.65
    elif sugar == 'Normal':
        total_price += (1 * drinks_num)
    elif sugar == 'Extra':
        total_price += (1.20 * drinks_num)
    if drinks_num >= 5:
        total_price *= 0.75
elif drink_kind == "Cappuccino":
    if sugar == 'Without':
        total_price += (1 * drinks_num) * 0.65
    elif sugar == 'Normal':
        total_price += (1.20 * drinks_num)
    elif sugar == 'Extra':
        total_price += (1.60 * drinks_num)
elif drink_kind == "Tea":
    if sugar == 'Without':
        total_price += (0.5 * drinks_num) * 0.65
    elif sugar == 'Normal':
        total_price += (0.60 * drinks_num)
    elif sugar == 'Extra':
        total_price += (0.70 * drinks_num)
        
if total_price > 15:
    total_price *= 0.80

print(f"You bought {drinks_num} cups of {drink_kind} for {total_price:.2f} lv.")
