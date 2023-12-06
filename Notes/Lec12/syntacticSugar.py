# Syntactic sugar
print(0)
def myDecorator(func):
    print(2)
    def wrapper():
        print(5)
        print("Something is happening before the function is called.")
        func()
        print(7)
        print("Something is happening after the function is called.")

    print(3)
    return wrapper

print(1)
@myDecorator  # Same as: sayWhee = myDecorator(sayWhee)
def sayWhee():
    print(6)
    print("Whee!")

print(4)
sayWhee()
print(8)
