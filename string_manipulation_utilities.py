def change_case(orig_string: str):
    return orig_string.swapcase()

def split_in_half(orig_string: str):
    mid = len(orig_string) // 2
    p1 = orig_string[:mid]
    p2 = orig_string[mid:]
    return p1, p2

def remove_special_characters(orig_string: str):
    sent = []
    for word in orig_string:
        if word.isalpha():
            sent.append(word)
        if word.isdigit():
            sent.append(word)
        if word == " ":
            sent.append(word)
        
    joined = "".join(sent)
    return joined
if __name__ == "__main__":
    print(change_case("meaN"))
    print(split_in_half("I feel so happy today"))
    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))
        


    

