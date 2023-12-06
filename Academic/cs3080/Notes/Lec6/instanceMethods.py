class Dog:
    species = 'mammal'  # Class attributes: same for all objs when creating them

    # Initializer / Instance attributes
    # Works just like a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def addLastname(self, lastname):
        self.name += ' ' + lastname


bella = Dog("Bella", 9)
print(bella.description())
lucy = Dog("Lucy", 4)
print(lucy.description())

lucy.addLastname('Liu')
print(lucy.description())


# something strange happens from here
print(bella.__dict__)
print(Dog.__dict__)

bella.species = "animal"   # you can change class attributes
print("{} is a {}!".format(bella.name, bella.species))
# Bella is a animal!
print("{} is a {}!".format(bella.name, Dog.species))
# Bella is a mammal!
print("{} is a {}!".format(lucy.name, lucy.species))
# Lucy is a mammal!

print(bella.__dict__)
print(lucy.__dict__)
print(Dog.__dict__)

