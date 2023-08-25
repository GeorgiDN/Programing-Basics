jury_number = int(input())
presentation = input()

assessment_sum = 0
total_assessment_sum = 0
assessment_counter = 0

while presentation != 'Finish':
    for i in range(jury_number):
        curr_assessment = float(input())
        assessment_sum += curr_assessment
        total_assessment_sum += curr_assessment
        assessment_counter += 1
    average_assessment = assessment_sum / jury_number
    print(f"{presentation} - {average_assessment:.2f}.")

    assessment_sum = 0
    presentation = input()

print(f"Student's final assessment is {total_assessment_sum / assessment_counter:.2f}.")
