n_distance = int(input())
time = input()
price = 0

taxi_initiation_fee = 0.70
taxi_daily_rate_km = 0.79
taxi_night_rate_km = 0.90

bus_daily_or_night_rate_km = 0.09

train_daily_or_night_rate_km = 0.06

if n_distance < 20 and time == 'day':
    price = taxi_initiation_fee + n_distance * taxi_daily_rate_km
elif n_distance < 20 and time == 'night':
    price = taxi_initiation_fee + n_distance * taxi_night_rate_km
elif 20 <= n_distance < 100:
    price = bus_daily_or_night_rate_km * n_distance
elif n_distance > 100:
    price = train_daily_or_night_rate_km * n_distance

print(f'{price:.2f}')
