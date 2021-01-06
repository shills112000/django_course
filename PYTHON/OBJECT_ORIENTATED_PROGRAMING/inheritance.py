#!/usr/local/bin/python3.7

#Inheritance

#form new classes using classes that have already been defined.

class Animal():   # Base class
    def __init__(self):
        print (f"animal created ")

    def who_am_i(self):
        print ("I am an animal")

    def eat(self):
        print ("I am eating")


class Dog(Animal):   # Dog inherits animal
    def __init__(self):
        Animal.__init__(self) # create instance of animal class when creating Dog class
        print ("Dog created")
    def who_am_i(self):
        print ("I am an dog")
    def bark(self):
        print ("Woof!")

my_dog= Dog()
my_dog.eat()  # the dog class can now inherits the method from the Animal class
my_dog.who_am_i()  # if the method is in dog it overwrites the inherited method from animal
my_dog.bark()

#myanimal = Animal()
#myanimal.eat()
#myanimal.who_am_i()

