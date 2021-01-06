#!/usr/local/bin/python3.7

from tires_class import Tire,SnowTire # Pull in the class from file tires_class.py

class Car:
    """
    Car models a car with tires and an engine
    """

    def __init__(self,tires,engine):
        self.engine = engine
        self.tires = tires

    def description(self):
        print (f"the car with an {self.engine} and {self.tires} tires")

    def wheel_circumference(self):
        if len (self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0

my_car = Car("test","test")
print (type (my_car))
print (my_car)

my_car = Car(['front-driver', 'front-passenger', 'rear-driver' , 'rear passenger'] ,"6stroke")
print (my_car)
my_car.description()


tire= SnowTire('P', 205, 65, 15, 2)
print (tire)
tires= [tire,tire,tire,tire]
honda= Car (tires=tires, engine='4-cylinder')
print (tire.circumference())
print (honda.description())
#print (honda.wheel_circumference())


tire= Tire('P', 205, 65, 15, 2)
tires= [tire,tire,tire,tire]
honda= Car (tires=tires, engine='4-cylinder')
print (tire.circumference())
print (honda.description())
#print (honda.wheel_circumference())

