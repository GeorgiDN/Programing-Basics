failed_threshold_times = int(input())

failed_times = 0
score_sum = 0
score_count = 0
last_problem = ''
has_failed = True


while failed_times < failed_threshold_times:
    task_name = input()
    if task_name == "Enough":
        has_failed = False
        break

    task_grade = int(input())

    score_sum += task_grade
    score_count += 1
    last_problem = task_name

    if task_grade <= 4:
        failed_times += 1
if has_failed:
    print(f'You need a break, {failed_times} poor grades.')
else:
    print(f'Average score: {score_sum / score_count:.2f}')
    print(f'Number of problems: {score_count}')
    print(f'Last problem: {last_problem}')
