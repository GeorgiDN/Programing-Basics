days = int(input())

treated_patients = 0
untreated_patients = 0
doctors = 7

for i in range(days):
    patients = int(input())
    if (i + 1) % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if patients <= doctors:
        treated_patients += patients
    elif patients > doctors:
        untreated_patients += patients - doctors
        treated_patients += doctors


print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
