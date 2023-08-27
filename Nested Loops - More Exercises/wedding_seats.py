last_sector = input()
rows_num_first_sector = int(input())
seats_num_odd_row = int(input())

seats_num_even_row = seats_num_odd_row + 2
counter_places = 0

for sector in range(ord('A'), ord(last_sector) + 1):
    for row in range(1, rows_num_first_sector + 1):
        if row % 2 != 0:  # Нечетен ред
            for seat in range(ord('a'), ord('a') + seats_num_odd_row):
                print(f"{chr(sector)}{row}{chr(seat)}")
                counter_places += 1
        else:  # Четен ред
            for seat in range(ord('a'), ord('a') + seats_num_even_row):
                print(f"{chr(sector)}{row}{chr(seat)}")
                counter_places += 1

    rows_num_first_sector += 1

print(counter_places)
