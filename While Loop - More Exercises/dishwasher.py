bottles_detergent = int(input())

total_detergent = bottles_detergent * 750

pots_num = 0
dishes_num = 0
load_counter = 1

while total_detergent > 0:
    command = input()
    if command == 'End':
        break
    curr_loading = int(command)
    if (load_counter % 3) == 0:
        pots_num += curr_loading
        total_detergent -= curr_loading * 15
    elif (load_counter % 3) != 0:
        dishes_num += curr_loading
        total_detergent -= curr_loading * 5
    load_counter += 1

if total_detergent > 0:
    print("Detergent was enough!")
    print(f"{dishes_num} dishes and {pots_num} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
  
