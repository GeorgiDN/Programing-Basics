budget_Peter = float(input())
video_cards_number = int(input())
processors_number = int(input())
ram_memory_number = int(input())

sum_of_video_cards = video_cards_number * 250
sum_of_processor = sum_of_video_cards * 0.35 * processors_number
sum_of_ram_memory = sum_of_video_cards * 0.1 * ram_memory_number

sum_needed = sum_of_video_cards + sum_of_processor + sum_of_ram_memory
if video_cards_number > processors_number:
    sum_needed *= 0.85

diff = abs(sum_needed - budget_Peter)

if budget_Peter >= sum_needed:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
