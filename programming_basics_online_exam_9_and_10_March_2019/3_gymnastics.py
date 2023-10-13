# https://judge.softuni.org/Contests/Practice/Index/1538#4
# Condition:https://judge.softuni.org/Contests/Practice/DownloadResource/5341

assessments = {
    "ribbon": {
        "Russia": {
            "difficulty": 9.100,
            "execution": 9.400,
        },
        "Bulgaria": {
            "difficulty": 9.600,
            "execution": 9.400,
        },
        "Italy": {
            "difficulty": 9.200,
            "execution": 9.500,
        }
    },
    "hoop": {
        "Russia": {
            "difficulty": 9.300,
            "execution": 9.800,
        },
        "Bulgaria": {
            "difficulty": 9.550,
            "execution": 9.750,
        },
        "Italy": {
            "difficulty": 9.450,
            "execution": 9.350,
        }
    },
    "rope": {
        "Russia": {
            "difficulty": 9.600,
            "execution": 9.000,
        },
        "Bulgaria": {
            "difficulty": 9.500,
            "execution": 9.400,
        },
        "Italy": {
            "difficulty": 9.700,
            "execution": 9.150,
        }
    },
}

country = input()
appliance = input()
max_points = 20

final_assessment = assessments[appliance][country]['difficulty'] + assessments[appliance][country]['execution']
difference_points_assessments = max_points - final_assessment
percent_not_enough_points = (difference_points_assessments / max_points) * 100

print(f"The team of {country} get {final_assessment:.3f} on {appliance}.")
print(f"{percent_not_enough_points:.2f}%")
