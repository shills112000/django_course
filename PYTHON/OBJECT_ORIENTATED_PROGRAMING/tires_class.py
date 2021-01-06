#!/usr/local/bin/python3.7
#from math import pi , just import one class
import math


class Tire:
    """
    Tire represents a tire that would be used in a car
    """

    def __init__(self, tire_type, width, ratio, diameter, brand='poop', construction='R'):
        self.tire_type =  tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def __repr__(self):
        """
        Respresent the tires info in the standard notation present
        on the side of the tire eg. 'P215/65R15'
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}"
                + f"{self.construction}{self.diameter}{self.brand}")

    def circumference(self):
        """
        The circumfereence of the tire in inches
        >>> tire = Tire('P', 205, 65, 15)~
        >>> tire.circumference()
        """
        #side_wall_inches = (self.width * (self.ratio / 100)) / 25.4
        total_diameter = self.side_wall_inches() * 2 + self.diameter #self._side_wall_inches calls the method
        return round(total_diameter * math.pi,1)

    def side_wall_inches(self):
        return (self.width * (self.ratio / 100)) / 25.4



class SnowTire(Tire): # this inherits from class Tire
    def __init__(self,tire_type, width, ratio, diameter , chain_thickness, brand ='', construction ='R'):
        #Tire.__init__(self ,tire_type, width, ratio, diameter ,brand , construction )
        super().__init__(tire_type, width, ratio, diameter ,brand , construction ) # inherit the Tire parent class __init__
        self.chain_thickness = chain_thickness

    def circumference(self):
        """
        Circ of tire snow chains in inches
        """
        total_diameter = (self.side_wall_inches() + self.chain_thickness ) * 2 + self.diameter
        return round(total_diameter * math.pi,1)

    def __repr__(self):
        return super().__repr__() + "(Snow)" # call the insherited class ___repr__


