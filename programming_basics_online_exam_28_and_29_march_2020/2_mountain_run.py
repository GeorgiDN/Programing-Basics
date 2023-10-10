# https://judge.softuni.org/Contests/Practice/Index/2275#3
#Condition: https://judge.softuni.org/Contests/Practice/DownloadResource/8856

from math import floor
record_in_second = float(input())
distance_in_meters = float(input())
time_in_seconds_climb_1m = float(input())

total_time = distance_in_meters * time_in_seconds_climb_1m
slowing_down = (distance_in_meters / 50)
slowing_down = floor(slowing_down)
slowing_down *= 30
final_time = total_time + slowing_down

difference = abs(final_time - record_in_second)

if final_time < record_in_second:
    print(f"Yes! The new record is {final_time:.2f} seconds.")
elif final_time >= record_in_second:
    print(f"No! He was {difference:.2f} seconds slower.")
