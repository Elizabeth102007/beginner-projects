import json

purpose = {"prosperity": "important", 
           "hapinness": "With God Help", 
           "freedom": "Prayer is the key"}


file_path = "/Users/elizabeth/Documents/note.json"
try:
    with open(file_path, "w") as f:
        json.dump(purpose, f, indent=4)
        print(f"'{file_path}' has been created!")
except FileExistsError:
    print("That file do exists")


with open(file_path, "r") as f:
    content = json.load(f)
    print(content)