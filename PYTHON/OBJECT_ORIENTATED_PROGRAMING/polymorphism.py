#!/usr/local/bin/python3.7

#Inheritance

#form new classes using classes that have already been defined.
# polymophism , refers to the way in different object classes can share same method name.

class Animal():   # Base class
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("subclass must implement this abstract method")

class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


max = Dog("max")
felix = Cat("felix")

print (f"{max.speak()}")
print (f"{felix.speak()}")

for pet in [max,felix]:
    print (type(pet))
    print (type(pet.speak()))
    print (pet.speak())


def pet_speak(pet):
    print (f"function pet_speak {pet.speak()}")


pet_speak(max)
pet_speak(felix)


my_animal=Animal('Fred')
my_animal.speak()


