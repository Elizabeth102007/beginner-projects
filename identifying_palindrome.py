def palindromes(word):
    reversed = word[::-1]
    if word == reversed:
        return True
    else:
        return False
def main():
    while True:
        ask = input("PLease enter a palindrome: ")
        if palindromes(ask):
            print(f"{ask} is a palindrome!")
            break

        else:
            print("that wasn't a palindrome")
            continue
main()




















