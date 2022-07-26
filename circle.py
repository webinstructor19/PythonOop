from cmath import pi


class Circle:
    def __init__(self , raduis):
        self.raduis = raduis

    def getRaduis(self):
        return self.raduis
    
    def setRaduis(self , raduis):
        self.raduis = raduis
    
    def circleArea(self):
        return pow(self.raduis , 2) * pi

    def circleCircumference(self):
        return 2 * pi * self.raduis

    def displayCircleInfo(self):
        print(f"Raduis = {self.raduis} \n Area = {self.circleArea()} \n Circumfernce = {self.circleCircumference()}")


cir = Circle(4)
cir.displayCircleInfo()