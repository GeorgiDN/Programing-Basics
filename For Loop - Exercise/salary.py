tabs_num = int(input())
salary = int(input())


for i in range(tabs_num):
    tabs = input()
    if tabs == "Facebook":
        salary -= 150
    elif tabs == "Instagram":
        salary -= 100
    elif tabs == "Reddit":
        salary -= 50

    if salary <= 0:
        break

if salary <= 0:
    print(f'You have lost your salary.')
else:
    print(salary)
