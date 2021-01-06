#!/usr/local/bin/python3.7


#https://docs.python.org/3/tutorial/classes.html#classes


# class allows us to define a type that allows functionaility
#defining own types using classes


# camelcase , CarModel
# """ this is documentation uses qutoes to stop and start

# __init__  , recreate a new instance method Dunder method

### OOP allows programmers to create their own objects that have methods and attributes


class Car:
    """
    Car models a car
    """

    def __init__(self, engine, tires, licence):
        self.engine = engine
        self.tires = tires
        self.licence = licence

    def print (self):
        print (self.tires)
        print (self.licence)

# pass just leaves the class
class Dog():

    # Class object attribute
    # Same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name,spots): # create init method , always called upon when you create a instance of the class
        # Attributes
        # We take in the argument
        # We assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots # Expect bolean True/False

    # OPERATIONS /Actions --> Methods
    def bark(self,number):  # the number paramter has to be called eg: my_dog.bark(1)
        print  (f"{self.name} is barking {number} times" )

#my_sample = Sample() # create an instance of class sample
my_dog = Dog(breed ='cocker',name='Max',spots="False" )
#my_dog = Dog(breed='woofer')
print (f"{my_dog}")
print (f"{my_dog.breed} {my_dog.name} {my_dog.spots} {my_dog.species}")

print (f"{my_dog.bark}") #  This just shows the object
my_dog.bark(44) # you need to use the brackets to call the method

class Circle():
    # Class object attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius=radius
        #self.area = radius * radius * self.pi
        self.area = radius * radius * Circle.pi # Circle.pi is the same as self.pi

    # Method
    def get_circumfrence(self):
        return self.radius * self.pi * 2

my_circle= Circle(30)
print (f" pi is:  {my_circle.pi} radius is : {my_circle.radius} circumfrence is :{my_circle.get_circumfrence()} area is : {my_circle.area} ")

