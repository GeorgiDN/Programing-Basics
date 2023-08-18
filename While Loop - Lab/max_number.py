import sys

max_number = - sys.maxsize

while True:
    command = input()
    if command == 'Stop':
        break
    curr_num = int(command)
    if curr_num > max_number:
        max_number = curr_num

print(max_number)
