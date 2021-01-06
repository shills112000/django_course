#!/usr/local/bin/python3.7


class Cyclinder():
    pi = 3.14159265359

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        volume = self.pi * self.radius ** 2 * self.height
        print (f" height is {self.height} , radius is {self.radius}")
        print (f" volume is : {volume} ")

    def surface_area(self):
        surface  =  2 * self.pi * self.radius * self.height + 2 * self.pi * self.radius ** 2
        print (f" height is {self.height} , radius is {self.radius}")
        print (f" surface area is : {surface} ")

my_cylinder = Cyclinder(5,5)

my_cylinder.volume()
my_cylinder.surface_area()
