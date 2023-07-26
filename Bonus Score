number_points = int(input())
bonus = 0

if number_points <= 100:
    bonus = 5
elif 100 < number_points <= 1000:
    bonus = 0.2 * number_points
elif number_points > 1000:
    bonus = 0.1 * number_points


if number_points % 2 == 0:
    bonus += 1
elif number_points % 10 == 5:
    bonus += 2

print(bonus)
print(number_points + bonus)
