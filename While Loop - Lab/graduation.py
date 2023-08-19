name = input()
grade_counter = 0
year_counter = 0
failed_year = 0

while True:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_year += 1

        if failed_year == 2:
            current_failed_year = year_counter + 1
            print(f"{name} has been excluded at {current_failed_year} grade")
            break

        continue

    year_counter += 1
    grade_counter += annual_grade

    if year_counter == 12:
        average_grade = grade_counter / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break
