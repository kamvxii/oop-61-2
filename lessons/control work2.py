#first task
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0
    def set_age(self, age):
        if age<0:
            print("You are not old enough")
        else:
            self.age = age
    def wew_age(self):
        return self.age
p=Person("John")
p.set_age(20)
print(p.wew_age())
p.set_age(-20)
print(p.wew_age())



#second task
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "I am an animal speaking"
class Dog(Animal):
    def speak(self):
        return 'woof'
class Cat(Animal):
    def speak(self):
        return 'meow'
print(Dog.speak())


#third task
class Vehicle:
    def move(self):
        return "Moving"
class Car(Vehicle):
    def move(self):
        return "car iscMoving"
class Truck(Vehicle):
    def move(self):
        return "Truck moving"
class Bike(Car):
    def move(self):
        return "Bike moving"
car=Car()
truck=Truck()
bike=Bike()
print(car.move())
print(truck.move())


#4 task
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
r=Rectangle(10,20)
c=Circle(5)
print(r.area())
print(c.area(),2)