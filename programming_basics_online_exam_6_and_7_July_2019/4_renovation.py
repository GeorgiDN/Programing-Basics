import math

height = int(input())
width = int(input())
percentageWindowsAndDoors = int(input())
input_str = input()
totalArea = height * width * 4
wallArea = totalArea - (totalArea / 100 * percentageWindowsAndDoors)
litersNeed = math.ceil(wallArea)
litersUsed = 0
totalLitersUsed = 0

while input_str != "Tired!":
    litersUsed = int(input_str)
    totalLitersUsed += litersUsed

    if totalLitersUsed == litersNeed:
        print(f"All walls are painted! Great job, Pesho!")
        break
    elif totalLitersUsed > litersNeed:
        print(f"All walls are painted and you have {totalLitersUsed - litersNeed} l paint left!")
        break

    input_str = input()

if input_str == "Tired!":
    print(f"{litersNeed - totalLitersUsed} quadratic m left.")
