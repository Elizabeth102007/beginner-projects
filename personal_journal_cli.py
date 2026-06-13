
file_path = "journal.txt"

def read_file():
    
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
    
    except FileNotFoundError:
        print("That file does not exist")

def write_file():
    data = input("Enter what you will like to add to your journal: ")

    count = count_entries()
    with open(file_path, "a") as file:
         file.write(f"Entry {count + 1}: {data}\n")

         print("Saved")


def count_entries():
    try: 
       with open(file_path) as file:
            count = 0
            for line in file:
                count += 1
            return count
    
    except FileNotFoundError:
        count = 0
        return count

def clear_journal():
    confirmation = input("Are you sure you want to clear yiur journal (y/n): ")
    if confirmation == "y":
       with open(file_path, "w") as file:
            file.write("")
            print("Journal cleared!")
    else:
        return

def menu():
    print("===========MY JOURNAL MENU=========")
    print("1. Write")
    print("2. Read")
    print("3. Count Entries")
    print("4. Clear")
    print("5. Exit")

def main():
    print(f"Total Entries: {count_entries()}")
    while True:
        menu()
        selection = input("Choose out of the options which action you will like to perform: ")
        if selection == "1":
            write_file()
        
        elif selection == "2":
            read_file()
        
        elif selection == "3":
            print(f"**Total Entries: {count_entries()}**")
        
        elif selection == "4":
            clear_journal()
        
        elif selection == "5":
            print("See ya!")
            break

if __name__ == "__main__":
    main()