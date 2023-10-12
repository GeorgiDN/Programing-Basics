# https://judge.softuni.org/Contests/Practice/Index/1538#3
# Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/5339

minutes_control = int(input())
seconds = int(input())
length_chute_m = float(input())
seconds_100m = int(input())

control_time_seconds = (minutes_control * 60) + seconds
time_slowing = length_chute_m / 120
total_time_slowing = time_slowing * 2.5

marin_time = (length_chute_m / 100) * seconds_100m - total_time_slowing

if marin_time <= control_time_seconds:
    print(f"Marin Bangiev won an Olympic quota!\n"
          f"His time is {marin_time:.3f}.")
else:
    diff = abs(marin_time - control_time_seconds)
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
