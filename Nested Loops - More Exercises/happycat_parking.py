days_total = int(input())
hours_total = int(input())

curr_day = 1
sum_per_day = 0
total_sum = 0

for day in range(1, days_total + 1):
    for hour in range(1, hours_total + 1):
        if day % 2 == 0 and hour % 2 != 0:
            total_sum += 2.50
            sum_per_day += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            total_sum += 1.25
            sum_per_day += 1.25
        else:
            total_sum += 1
            sum_per_day += 1

    print(f"Day: {day} - {sum_per_day:.2f} leva")
    curr_day += 1
    sum_per_day = 0


print(f"Total: {total_sum:.2f} leva")
