import csv
file_path = "grades.csv"
def load_file():
   try: 
       with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
   
   except FileNotFoundError:
       return []

students = load_file()

def save_file(students):
    with open(file_path, "w", newline="") as file:
        fieldnames = ["name", "math", "english", "science"]
        
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        

        writer.writeheader()

        for student in students:
            writer.writerow(student)


def add_details(students):
    name = input("Enter your name: ").lower()
    math = input("Enter your math score: ")
    english = input("Enter your english score: ")
    science = input("Enter your science score: ")

    course = {"name" : name,
              "math" : math,
              "english" : english,
              "science" : science}
    
    students.append(course)
    print("Student update done!")

def view_details(students):
    if not students:
        print("No student details added")
    else:
        for student in students:
            print(f"Name: {student['name'].title()}")
            print(f"Mathematics: {student['math']}")
            print(f"English: {student['english']}")
            print(f"Science: {student['science']}")
            total = int(student['math']) + int(student['english']) + int(student['science'])
            print(f"Total Average : {total/3:.2f}")

def search_student(students):
    name_search = input("Enter the name you want to search for: ")
    search = False
    for student in students:
        if student['name'] == name_search.lower():
            print("Name found!")
            print(f"Name: {student['name'].title()}")
            print(f"Mathematics: {student['math']}")
            print(f"English: {student['english']}")
            print(f"Science: {student['science']}")
            search = True
            break
    if not search:
        print(f"{name_search} not found.")

def delete_student(students):
    name_delete = input("Enter the name you want to delete: ")
    delete = False
    for student in students:
        if student['name'] == name_delete.lower():
            students.remove(student)
            print("Student details deleted")
            delete = True
            break
    if not delete:
        print(f"{name_delete} not found.")

def show_menu():
    print("===========================")
    print("1. Add Student details")
    print("2. View Student details")
    print("3. Search Student details")
    print("4. Delete Student details")
    print("0. Exit")
    print("============================")

def main():
    print(f"Total Students: {len(students)}")
    while True:
        show_menu()
        option = input("Select the action you would like to perform: ")
        
        if option == "1":
            add_details(students)
            save_file(students)
        
        elif option == "2":
            view_details(students)
        
        elif option == "3":
            search_student(students)
        
        elif option == "4": 
            delete_student(students)
            save_file(students)
        
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()




