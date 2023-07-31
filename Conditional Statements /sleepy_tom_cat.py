rest_days = int(input())

holidays_playing_minutes = rest_days * 127
working_days_playing_minutes = (365 - rest_days) * 63
total_time = abs(holidays_playing_minutes + working_days_playing_minutes)

playing_time = abs(30000 - (holidays_playing_minutes + working_days_playing_minutes))
hours = playing_time // 60
minutes = playing_time % 60

if 30000 > total_time:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
