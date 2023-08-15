students_num = int(input())

top_students = 0
good_students = 0
middle_students = 0
fail_students = 0
sum_of_evaluation = 0

for i in range(students_num):
    evaluation = float(input())
    if evaluation >= 5:
        top_students += 1
        sum_of_evaluation += evaluation
    elif 4 <= evaluation <= 4.99:
        good_students += 1
        sum_of_evaluation += evaluation
    elif 3 <= evaluation <= 3.99:
        middle_students += 1
        sum_of_evaluation += evaluation
    elif 2 <= evaluation <= 2.99:
        fail_students += 1
        sum_of_evaluation += evaluation

average_success = sum_of_evaluation / students_num

percent_top_students = top_students / students_num * 100
percent_good_students = good_students / students_num * 100
percent_middle_students = middle_students / students_num * 100
percent_fail_students = fail_students / students_num * 100

print(f'Top students: {percent_top_students:.2f}%')
print(f'Between 4.00 and 4.99: {percent_good_students:.2f}%')
print(f'Between 3.00 and 3.99: {percent_middle_students:.2f}%')
print(f'Fail: {percent_fail_students:.2f}%')
print(f'Average: {average_success:.2f}')
