record_sec = float(input())
meters_dist = float(input())
time_swim_1_meter = float(input())

swimming_time = meters_dist * time_swim_1_meter
slowing_down = meters_dist // 15 * 12.5
total_time = swimming_time + slowing_down

diff = abs(total_time - record_sec)

if total_time < record_sec:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')
