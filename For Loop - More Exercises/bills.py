months = int(input())

electricity = 0
water = 0
internet = 0
others_total = 0

for i in range(months):
    electricity_bill = float(input())
    electricity += electricity_bill
    water += 20
    internet += 15
    others = electricity + water + internet + ((electricity + water + internet) * 0.2)
    others_total = others

total_sum = electricity + water + internet + others_total
average_sum = total_sum / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others_total:.2f} lv")
print(f"Average: {average_sum:.2f} lv")
