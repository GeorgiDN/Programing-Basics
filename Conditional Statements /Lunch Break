import math

serial = input()
duration_episode = int(input())
duration_break = int(input())

lunch_time = 0.125 * duration_break
recreation_time = 0.25 * duration_break

time_for_movie = duration_break - lunch_time - recreation_time

if time_for_movie >= duration_episode:
    print(f"You have enough time to watch {serial} and left with {math.ceil(time_for_movie - duration_episode)} "
          f"minutes free time.")
else:
    print(f"You don't have enough time to watch {serial}, you need {math.ceil(duration_episode - time_for_movie)} "
          f"more minutes.")
