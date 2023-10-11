# https://judge.softuni.org/Contests/Practice/Index/2275#9
# Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/8868

suitcases_loaded = 0
capacity = float(input())
suitcases_counter = 0
loaded_suitcases = True

while True:
    command = input()
    if command == "End":
        break
    suitcase_volume = float(command)

    suitcases_counter += 1
    if suitcases_counter % 3 == 0:
        suitcase_volume *= 1.10

    if suitcase_volume > capacity:
        loaded_suitcases = False
        break

    suitcases_loaded += 1
    capacity -= suitcase_volume

if loaded_suitcases:
    print("Congratulations! All suitcases are loaded!")
elif not loaded_suitcases:
    print("No more space!")

print(f"Statistic: {suitcases_loaded} suitcases loaded.")
