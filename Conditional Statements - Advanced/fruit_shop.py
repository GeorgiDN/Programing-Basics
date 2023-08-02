fruit = input()
day_of_week = input()
quantity = float(input())

price = 0
FALSE_DATA = False

valid_fruits = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']
valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

if fruit not in valid_fruits or day_of_week not in valid_days:
    FALSE_DATA = True

if fruit == 'banana':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
    or day_of_week == 'Friday':
        price = quantity * 2.50
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 2.70
    else:
        FALSE_DATA = True
elif fruit == 'apple':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
    or day_of_week == 'Friday':
        price = quantity * 1.20
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 1.25
    else:
        FALSE_DATA = True
elif fruit == 'orange':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
    or day_of_week == 'Friday':
        price = quantity * 0.85
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 0.90
    else:
        FALSE_DATA = True
elif fruit == 'grapefruit':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
    or day_of_week == 'Friday':
        price = quantity * 1.45
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 1.60
    else:
        FALSE_DATA = True
elif fruit == 'kiwi':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
    or day_of_week == 'Friday':
        price = quantity * 2.70
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 3.00
    else:
        FALSE_DATA = True
elif fruit == 'pineapple':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
    or day_of_week == 'Friday':
        price = quantity * 5.50
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 5.60
    else:
        FALSE_DATA = True
elif fruit == 'grapes':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' \
            or day_of_week == 'Friday':
        price = quantity * 3.85
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = quantity * 4.20
    else:
        FALSE_DATA = True

if not FALSE_DATA:
    print(f'{price:.2f}')
else:
    print('error')


