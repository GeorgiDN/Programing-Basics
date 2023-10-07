from math import ceil
people_num = int(input())
enter_fee = float(input())
sunbed_fee = float(input())
umbrella_fee = float(input())

enter_fee_total = enter_fee * people_num

sunbed_number = ceil(people_num * 0.75)
sunbed_fee_total = sunbed_number * sunbed_fee

umbrella_number = ceil(people_num * 0.5)
umbrella_fee_total = umbrella_number * umbrella_fee

total_price = enter_fee_total + sunbed_fee_total + umbrella_fee_total
print(f"{total_price:.2f} lv.")
