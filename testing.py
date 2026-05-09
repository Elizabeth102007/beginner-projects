def no_shouting(uppers):
    new_list = []

    for upper in uppers:
        if not upper.isupper():
            new_list.append(upper)
    return new_list

if __name__ == '__main__':
   print(no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]))



















