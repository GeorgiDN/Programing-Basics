#https://judge.softuni.org/Contests/Practice/Index/1538#10
# Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/13609

def jump_successful(h, j):
    if j > h:
        return True
    elif j <= h:
        return False

tihomir_aim = int(input())
jumps_number = 0
fail = False
bar_height = tihomir_aim - 30
while True:
    attempt = 3

    while attempt > 0:
        jump = int(input())
        jumps_number += 1
        if jump_successful(bar_height, jump):
            bar_height += 5
            break
        elif not jump_successful(bar_height, jump):
            attempt -= 1
            if attempt == 0:
                fail = True
                break

    if fail:
        break
    if bar_height > tihomir_aim:
        break

if not fail:
    print(f"Tihomir succeeded, he jumped over {tihomir_aim}cm after {jumps_number} jumps.")
elif fail:
    print(f"Tihomir failed at {bar_height}cm after {jumps_number} jumps.")
