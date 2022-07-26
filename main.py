'''
4 Pillars
Encapsulation => how object does something 
Abstraction => what object does something
Inheritance => 
Polymorphism => overload => add(x , y) add(x , y , z)
override => area () : length * width
            area() : pow(r , 2) * pi

class User{
    public User(){

    } 
}

User user = new User();

void sayWelcome(){return }
int sum(){return 10;}
'''
class User:
    # Attributes , data member , fields ===> variable
    # constructor => dunder methods ==> __init__()
    # Default constructor
    # parmterized constructor
    def __init__(self , name , passwd):
        self.username = name
        self.password = passwd
        print('From First Init')

    # return string representaion of an object 
    def __str__(self):
        return f"Username is {self.username} , Password is {self.password}"


user1 = User('omnia' , '123')
user2 = User('sara' , '456')
print(user1)


class Rectangle:
    def __init__(self , length , width):
        self._length = length
        self._width = width
    # Method to calc rectangle area
    def rectangleArea(self):
        return self.length * self.width
    #method to calc rectangle perimeter
    def rectanglePerimeter(self):
        return (self.length + self.width) * 2

'''
rect = Rectangle(5 , 2)
print(rect.rectanglePerimeter())
print(rect.rectangleArea())
'''
# python support multiple inheritance
#Parent Class , Super Class 
class Person:
    name = ''
    age = ''
    address = ''
    
    def Eat(self):
        print('Every person eat ...')
# Child Class , Sub Class , Derived Class 
class Doctor(Person):
    pass

class Engineer(Person):
    def test(self):
        print('hello from test func')


class Dentist(Engineer , Doctor):
    pass
# double raduis
den = Dentist()
den.Eat()
den.test()

d = Doctor()
d.Eat()

e = Engineer()
e.Eat()