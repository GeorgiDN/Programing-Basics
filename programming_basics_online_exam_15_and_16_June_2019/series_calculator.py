from math import floor
serial_name = input()
seasons = int(input())
episodes = int(input())
duration_with_no_advertisements = float(input())

advertisements_duration = duration_with_no_advertisements * 0.20
duration_one_episode_with_advertisements = duration_with_no_advertisements + advertisements_duration

additional_time_last_episode = 10 * seasons

total_time = duration_one_episode_with_advertisements * episodes * seasons + additional_time_last_episode

total_time = floor(total_time)

print(f"Total time needed to watch the {serial_name} series is {total_time} minutes.")
