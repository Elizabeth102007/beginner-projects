def add_course(courses):
    name = input("course: ")
    grade = int(input("grade: "))
    credits = int(input("credits: "))

    if name not in courses:
        courses[name] = {"grade": grade, "credits": credits}
    else:
        if grade > courses[name]["grade"]:
            courses[name]["grade"] = grade

def get_course(courses):
    name = input("course: ")
    
    if name not in courses:
        print("no entry for this course")
    else:
        print(f"{name} ({courses[name]['credits']} cr) grade {courses[name]['grade']}")

def statistics(courses):
    count = len(courses)
    total_credits = sum(courses[name]["credits"] for name in courses)
    mean = sum(courses[name]["grade"] for name in courses) / count
    
    print(f"{count} completed courses, a total of {total_credits} credits")
    print(f"mean {mean:.1f}")
    print("grade distribution")
    for g in range(5, 0, -1):
        students = [name for name in courses if courses[name]["grade"] == g]
        print(f"{g}: {'x' * len(students)}")

def menu():
    print("1 add course")
    print("2 get course data")
    print("3 statistics")
    print("0 exit")
def main():
    courses = {}
    
    while True:
        menu()
        command = int(input("command: "))
        
        if command == 1:
            add_course(courses)
        elif command == 2:
            get_course(courses)
        elif command == 3:
            statistics(courses)
        elif command == 0:
            break

main()
            
               
               
               
               
              
