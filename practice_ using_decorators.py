def announce(func):

    def wrapper(*args, **kwargs):

        print("Starting.....")

        func(*args, **kwargs)

        print("Finished.....")

    return wrapper

@announce
def greet(name):
    print(f"Hello {name}")

greet("Jenny")

