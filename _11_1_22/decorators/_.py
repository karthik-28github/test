#chain linking decorator
def arrow(func):
    def wrapper():
        print("--> --> --> -->")
        func()
        print("--> --> --> -->")
    return wrapper


def dotted(func):
    def wrapper():
        print("--- --- --- ---")
        func()
        print("--- --- --- ---")

    return wrapper

@arrow
@dotted
def display():
    print("KarthiK")
