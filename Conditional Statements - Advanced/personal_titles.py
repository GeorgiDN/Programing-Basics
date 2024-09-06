age = float(input())
gender = input()

if gender == 'm':
    if age >= 16:
        print('Mr.')
    else:
        print('Master')
elif gender == 'f':
    if age >= 16:
        print('Ms.')
    else:
        print('Miss')


##################################################################################
age = float(input())
gender = input()

title = 'Mr.' if gender == 'm' and age >= 16 else 'Master' \
    if gender == 'm' else 'Ms.' if gender == 'f' and age >= 16 else 'Miss'

print(title)


##################################################################################
age, gender = float(input()),  input()
print('Mr.' if gender == 'm' and age >= 16 else 'Master' if gender == 'm' else 'Ms.' if gender == 'f' and age >= 16 else 'Miss')



##################################################################################
def personal_titles(*args):
    age = float(args[0]),
    gender = args[1]

    dictionary = {
        "m": [
            {"min": 16, "title": "Mr."},
            {"min": 0, "title": "Master"},
        ],
        "f": [
            {"min": 16, "title": "Ms."},
            {"min": 0, "title": "Miss"},
        ]
    }

    for curren_age in dictionary[gender]:
        if age >= curren_age["min"]:
            return print(curren_age["title"])


age, gender = float(input()), input()
personal_titles(age, gender)
