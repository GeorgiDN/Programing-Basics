city = input()
sales_volume = float(input())

commission = 0

if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        commission = sales_volume * 0.05
    elif 500 <= sales_volume <= 1000:
        commission = sales_volume * 0.07
    elif 1000 <= sales_volume <= 10000:
        commission = sales_volume * 0.08
    elif sales_volume > 10000:
        commission = sales_volume * 0.12
elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        commission = sales_volume * 0.045
    elif 500 <= sales_volume <= 1000:
        commission = sales_volume * 0.075
    elif 1000 <= sales_volume <= 10000:
        commission = sales_volume * 0.10
    elif sales_volume > 10000:
        commission = sales_volume * 0.13
elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        commission = sales_volume * 0.055
    elif 500 <= sales_volume <= 1000:
        commission = sales_volume * 0.08
    elif 1000 <= sales_volume <= 10000:
        commission = sales_volume * 0.12
    elif sales_volume > 10000:
        commission = sales_volume * 0.145

if sales_volume > 0 and commission > 0:
    print(f'{commission:.2f}')
elif sales_volume <= 0 or city not in ['Sofia', 'Varna', 'Plovdiv']:
    print('error')
