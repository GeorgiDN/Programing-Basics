import sys

min_number = sys.maxsize

while True:
    command = input()
    if command == 'Stop':
        break
    curr_num = int(command)
    if curr_num < min_number:
        min_number = curr_num

print(min_number)
