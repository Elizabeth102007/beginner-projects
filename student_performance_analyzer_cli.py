def students_list():
    students = {
        "Mia":
            {"Geometry": 67,
             "Neuroscience": 75,
             "Geography": 85,
             "Anatomy": 20},
        "Henry":
            {"Geometry": 34,
             "Neuroscience": 75,
             "Geography": 85,
             "Anatomy": 25},
        "Jasmine":
            {"Geometry": 50,
             "Neuroscience": 33,
             "Geography": 40,
             "Anatomy": 35},
        "Eliza":
            {"Geometry": 70,
             "Neuroscience": 75,
             "Geography": 65,
             "Anatomy": 26},
        "Becky":
            {"Geometry": 25,
             "Neuroscience": 42,
             "Geography": 70,
             "Anatomy": 30},
        "Emerald":
            {"Geometry": 67,
             "Neuroscience": 75,
             "Geography": 85,
             "Anatomy": 60}
    }
    return students


def calculate_median(grades):
    sorting = sorted(grades)
    n = len(sorting)
    mid = n // 2
    if n % 2 == 0:
        return (sorting[mid] + sorting[mid - 1]) / 2
    else:
        return sorting[mid]


def calculate_weighted_gpa(subject_data):
    credit_points = {"Geometry": 0.4, "Neuroscience": 0.3, "Geography": 0.2, "Anatomy": 0.1}
    total_points = 0.0
    total_weights = 0.0
    for subject, score in subject_data.items():
        if subject in credit_points:
            weight = credit_points[subject]
            total_points += score * weight
            total_weights += weight

    return round(total_points / total_weights, 2)


def calculate_scores(students):
    student_results = {}
    all_averages = []

    for name, subject_data in students.items():
        grades = subject_data.values()

        average = sum(grades) / len(grades)
        highest = max(grades)
        lowest = min(grades)
        all_averages.append(average)
        median = calculate_median(grades)
        weighted_gpa = calculate_weighted_gpa(subject_data)
        student_results[name] = {
            "average": average,
            "status" : "Pass" if average >=50 else "Fail",
            "highest_score": highest,
             "lowest_score": lowest,
            "median": median,
            "weighted_gpa": weighted_gpa,
        }

    return student_results


def find_failing_students(students):
    failed_students = set()
    for name, subject_data in students.items():

        failed_subjects = {subject for subject, score in subject_data.items() if score <=40 }
        if len(failed_subjects) >=2:
            failed_students.add(name)
    return failed_students


def print_leaderboard(students):
    student_results = calculate_scores(students)
    sorted_students = sorted(student_results.items(), key=lambda item: item[1]["average"], reverse=True)
    for rank, (name, score) in enumerate(sorted_students, start=1):
        filled = int((score["average"] / 100) * 20)
        empty = 20 - filled
        bar = "█" * filled + "░" * empty

        print(f"{rank}. {name:<10} | Weighted GPA: {score['weighted_gpa']} |Average: {score['average']} | Median: {score['median']} | Highest Score: {score['highest_score']} | Lowest Score: {score['lowest_score']} | {score['status']} | ({bar})")



def subject_average(students):
    subject_scores = {}

    for student, subjects in students.items():

        for subject, score in subjects.items():

            if subject not in subject_scores:
                subject_scores[subject] = []

            subject_scores[subject].append(score)

    print("Subject Scores:")
    print(subject_scores)
    print()
    print("Subject Averages:")

    for subject, scores in subject_scores.items():
        average = sum(scores) / len(scores)
        print(f"{subject}: {average:.2f}")

    print("\nFlagged Subjects:")
    for subject, scores in subject_scores.items():
        failing_students = 0
        pass_mark = 50
        for score in scores:
              if score <= pass_mark:
                 failing_students += 1

        if failing_students > len(scores) / 2:
              print(f"{subject} has majority failing.")




def menu():
    print("1. Show Failing Students")
    print("2. Show subject averages and subject with the highest failure")
    print("3. Show Leaderboard")
    print("4. Quit")
def main():
    students = students_list()

    while True:
        menu()
        options = input("Enter your choice based on what you will love to work on (1, 2, 3, 4):")
        if options == "1":
            print(find_failing_students(students))

        elif options == "2":
            subject_average(students)

        elif options == "3":
            print_leaderboard(students)

        elif options == "4":
            break

        else:
            print("Invalid choice, read the options again.")
if __name__ == "__main__":
    main()















