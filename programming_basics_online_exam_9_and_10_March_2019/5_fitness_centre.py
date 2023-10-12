# https://judge.softuni.org/Contests/Practice/Index/1538#9
# condition:https://judge.softuni.org/Contests/Practice/DownloadResource/5351

visitors_number = int(input())

numbers_people_workout = {"Back": 0, "Chest": 0, "Legs": 0, "Abs": 0}
numbers_people_protein = {"Protein shake": 0, "Protein bar": 0}

for num in range(visitors_number):
    activity = input()
    if activity in numbers_people_workout:
        numbers_people_workout[activity] += 1
    elif activity in numbers_people_protein:
        numbers_people_protein[activity] += 1

work_out_numbers = list(numbers_people_workout.values())
sum_people_workout = sum(work_out_numbers)
protein_numbers = list(numbers_people_protein.values())
sum_people_protein = sum(protein_numbers)

percent_people_workout = (sum_people_workout / visitors_number) * 100
percent_people_protein = (sum_people_protein / visitors_number) * 100

for workout, count in numbers_people_workout.items():
    print(f"{count} - {workout.lower()}")
for protein, count1 in numbers_people_protein.items():
    print(f"{count1} - {protein.lower()}")

print(f"{percent_people_workout:.2f}% - work out")
print(f"{percent_people_protein :.2f}% - protein")




################################################################################################################################################################################################

# visitors_number = int(input())
# numbers_people_workout = {"Back": 0, "Chest": 0, "Legs": 0, "Abs": 0}
# numbers_people_protein = {"Protein shake": 0, "Protein bar": 0}
#
# for num in range(visitors_number):
#     activity = input()
#     if activity in numbers_people_workout:
#         numbers_people_workout[activity] += 1
#     elif activity in numbers_people_protein:
#         numbers_people_protein[activity] += 1
#
# work_out_numbers = list(numbers_people_workout.values())
# sum_people_workout = sum(work_out_numbers)
# protein_numbers = list(numbers_people_protein.values())
# sum_people_protein = sum(protein_numbers)
# percent_people_workout = (sum_people_workout / visitors_number) * 100
# percent_people_protein = (sum_people_protein / visitors_number) * 100
#
# back = numbers_people_workout["Back"]
# chest = numbers_people_workout["Chest"]
# legs = numbers_people_workout["Legs"]
# abss = numbers_people_workout["Abs"]
# protein_shake = numbers_people_protein["Protein shake"]
# protein_bar = numbers_people_protein["Protein bar"]
#
# print(f"{back} - back")
# print(f"{chest} - chest")
# print(f"{legs} - legs")
# print(f"{abss} - abs")
# print(f"{protein_shake} - protein shake")
# print(f"{protein_bar} - protein bar")
# print(f"{percent_people_workout:.2f}% - work out")
# print(f"{percent_people_protein :.2f}% - protein")
