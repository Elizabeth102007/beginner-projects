import csv
# writing
body_goals = [["Name", "Age", "Target_body_weight"], 
              ["Jenny", 25, 55], 
              ["Olivia", 40, 57], 
              ["Zara", 33, 60]]

file_path = "/Users/elizabeth/Documents/body_goals.csv"

try:
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        for row in body_goals:
            writer.writerow(row)
        print(f"'{file_path}' has been created!")

except FileExistsError:
    print("That file do exists")
# reading
with open(file_path, "r") as f:
    content = csv.reader(f)
    for line in content:
        print(line)
    
    