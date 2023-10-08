from math import ceil
wall_height = int(input())
wall_width = int(input())
percent_input = int(input())
percent_non_painted_walls = percent_input / 100

total_area_for_painting = (wall_height * wall_width * 4)
total_area_for_painting -= total_area_for_painting * percent_non_painted_walls
liters_paint = 0

while True:
    command = input()
    if command == "Tired!":
        print(f"{ceil(total_area_for_painting)} quadratic m left.")
        break

    liters_paint = int(command)
    total_area_for_painting -= liters_paint

    if total_area_for_painting <= 0:
        if liters_paint <= 0:
            print("All walls are painted! Great job, Pesho!")
            break
        elif liters_paint > 0:
            total_area_for_painting = abs(total_area_for_painting)
            total_area_for_painting = ceil(total_area_for_painting)
            print(f"All walls are painted and you have {total_area_for_painting} l paint left!")
            break
