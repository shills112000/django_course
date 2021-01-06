#!/usr/local/bin/python3.7

class Line():
    def __init__(self,coord1,coord2):
        self.coord1 = coord1
        self.coord2 = coord2
        self.x1,self.y1 = self.coord1
        self.x2,self.y2 = self.coord2
       # x1= self.coord1[0]
       # y1= self.coord1[1]
       # x2= self.coord2[0]
       # y2= self.coord2[1]
        # or  x1,y1 = self.cord1
        # or x2,y2 = self.cord2

    def distance(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        print (self.coord1)
        print (f" x1 is {x1} y1 is {y1}")
        print (f" x2 is {x2} y2 is {y2}")
        distance= ((x2 - x1) **2 + (y2 - y1) **2 ) ** 0.5
        print (f" distance is {distance}")
        #d = sqroot of  (x2 - x1) + (y2 - ya)**2

    def slope(self):
        slope = (self.y2-self.y1) / (self.x2 - self.x1)
        print (f" slope is {slope}")

coord1 = (3,2)
print (coord1)
coord2 = (8,10)

li = Line(coord1, coord2)
li.distance()
li.slope()
