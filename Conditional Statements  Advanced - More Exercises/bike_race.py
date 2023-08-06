juniors = int(input())
seniors = int(input())
track = input()

fee = 0

if track == 'trail':
    fee = (juniors * 5.50) + (seniors * 7)
    fee *= 0.95
elif track == 'cross-country':
    fee = (juniors * 8) + (seniors * 9.50)
    fee *= 0.95
    if (juniors + seniors) >= 50:
        fee *= 0.75
elif track == 'downhill':
    fee = (juniors * 12.25) + (seniors * 13.75)
    fee *= 0.95
elif track == 'road':
    fee = (juniors * 20) + (seniors * 21.50)
    fee *= 0.95

print(f'{fee:.2f}')
