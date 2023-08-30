groups_num = int(input())

Musala_climbers = 0
Mont_Blanc_climbers = 0
Kilimandjaro_climbers = 0
K2_climbers = 0
Everest_climbers = 0

total_num_climbers = 0

for i in range(groups_num):
    climbers_num = int(input())
    total_num_climbers += climbers_num
    if climbers_num <= 5:
        Musala_climbers += climbers_num
    elif 6 <= climbers_num <= 12:
        Mont_Blanc_climbers += climbers_num
    elif 13 <= climbers_num <= 25:
        Kilimandjaro_climbers += climbers_num
    elif 26 <= climbers_num <= 40:
        K2_climbers += climbers_num
    elif climbers_num >= 41:
        Everest_climbers += climbers_num

print(f'{(Musala_climbers / total_num_climbers) * 100:.2f}%')
print(f'{(Mont_Blanc_climbers / total_num_climbers) * 100:.2f}%')
print(f'{(Kilimandjaro_climbers / total_num_climbers) * 100:.2f}%')
print(f'{(K2_climbers / total_num_climbers) * 100:.2f}%')
print(f'{(Everest_climbers / total_num_climbers) * 100:.2f}%')
