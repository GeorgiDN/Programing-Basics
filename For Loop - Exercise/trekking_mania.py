climbers_groups = int(input())

mussalla = 0
montblank = 0
kilimanjaro = 0
k2 = 0
everest = 0

for i in range(climbers_groups):
    climbers_number = int(input())
    if climbers_number <= 5:
        mussalla += climbers_number
    elif 6 <= climbers_number <= 12:
        montblank += climbers_number
    elif 13 <= climbers_number <= 25:
        kilimanjaro += climbers_number
    elif 26 <= climbers_number <= 40:
        k2 += climbers_number
    elif climbers_number >= 41:
        everest += climbers_number

total_climbers_number = mussalla + montblank + kilimanjaro + k2 + everest

percent_climbers_mussalla = mussalla / total_climbers_number * 100
percent_climbers_montblank = montblank / total_climbers_number * 100
percent_climbers_kilimanjaro = kilimanjaro / total_climbers_number * 100
percent_climbers_k2 = k2 / total_climbers_number * 100
percent_climbers_everest = everest / total_climbers_number * 100

print(f'{percent_climbers_mussalla:.2f}%')
print(f'{percent_climbers_montblank:.2f}%')
print(f'{percent_climbers_kilimanjaro:.2f}%')
print(f'{percent_climbers_k2:.2f}%')
print(f'{percent_climbers_everest:.2f}%')
