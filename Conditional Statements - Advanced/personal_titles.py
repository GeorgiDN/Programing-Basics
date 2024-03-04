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



# Do not do this!
        
# age = float(input())
# gender = input()

# title = 'Mr.' if gender == 'm' and age >= 16 else 'Master' \
#     if gender == 'm' else 'Ms.' if gender == 'f' and age >= 16 else 'Miss'

# print(title)



# age, gender = float(input()),  input()
# print('Mr.' if gender == 'm' and age >= 16 else 'Master' if gender == 'm' else 'Ms.' if gender == 'f' and age >= 16 else 'Miss')
