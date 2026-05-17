def invert(dictionary: dict):
    inverted = {value: key for key, value in dictionary.items()}
    dictionary.clear()
    dictionary.update(inverted)
    print(dictionary)
if __name__=="__main__":
    invert({1: "first", 2: "second", 3: "third", 4: "fourth"})