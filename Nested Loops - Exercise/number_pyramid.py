n = int(input())
curr_number = 1
is_finished = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if curr_number > n:
            is_finished = True
            break

        print(curr_number, end=' ')
        curr_number += 1

    if is_finished:
        break
    print()
