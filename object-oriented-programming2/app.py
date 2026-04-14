# oop programming part 2 
# polymorphism, inheritance, abstraction
# we laearn how classed relate to each other .and how the tool behaves 

# INHERITANCE: allows a child to acquire the attributes and methods of a parent class. Use super() to call the parent __init__ from the child , so you dont have 
# to rewrite shared setup code.

# EXAMPLE: 

# parent class
# class Animal: # base class 
#     def __init__(self, name, age): # constructor
#         self.name = name
#         self.age = age
        
#     def describe(self):
#         print(f'{self.name} is {self.age} years old')
    
#     def speak(self): # default speak method
#         print('---')

# # child classes - inherites from the parent class called animal
# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age) # call parent__init__
#         self.breed = breed
    
#     def speak(self): # overrride parent method
#         print(f'{self.name} says Woof!')

# class Cat(Animal):
#     def speak(self):
#         print(f'{self.name} says: Meow!')

# class Bird(Animal):
#     def speak(self):
#         print(f'{self.name} says: Tweet!')

# print()
# # Usage 
# dog = Dog('jules', 16, 'alsatian')
# cat = Cat('mark', 15)
# bird = Bird('Tweety', 3)

# dog.describe()
# dog.speak()
# cat.speak()
# bird.speak()

# print()


# # SUPER 
# # __str__ override - controls whta prints(object) shows
# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed

#     def __str__(self):
#         return f'Dog: {self.name}, Age: {self.age} Breed: {self.breed}'
    
#     def speak(self)
#         print(f'{self.name} says : Woof!')
    
# # create dog object
# dog = Dog('Rex' , 3 , 'chiwawa')
# # calls __str__, outputs : Dog, Rx, Age
# print(dog)

# # isinstance() - check if object is instance of a class
# print(isinstance(dog, jbDog))
# print(isinstance(dog, Animal))
# print(isinstance(dog, Cat))


# print()


# PLOYMORPISM - means the same methos name behaved diffresbtly dpendong on which class it belongs to 
# this alows you to write code that works on my object that has a particular method - without caring about the specific class

# Example on polymorphism : 
# same function on all animal types 

# def make_sound(animal):
#     animal.speak() # calls the right speak() for each class

# animals = [Dog('Rex', 3, 'lab'), Cat('Whiskers', 5) , Bird('Tweety', 2)]

# for x in animals:
#     make_sound(x)
    


# another example on polymorpism
print()
# Shapes example - polymorpism with area()

# class Shape:
#     def area(self):
#         return 0
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14159 * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#     def area(self):
#         return self.w * self.h
    

# shapes = [Circle(5), Rectangle(4,6)]
# for x in shapes:
#     print(f'Area: {x.area()}')

# # OR 

# shape1 = [Circle(5)]
# shape2 = [Rectangle(4,6)]
# for x in shape1:
#     print(f'Area of Circle: {x.area():.2f}')
# for x in shape2:
#     print(f'Area of Triangle: {x.area()}')

# print()


# Abstarction : hides internal implementation details and expense : only what is nessecasy in python abstarct base classes (abc)
# enforce that : child classes implement certain methods you cannot instaciacean abstarct class directly 

# example 
from abc import ABC, abstractmethod

class Shape(ABC): # distract base class
    @abstractmethod
    def area(self):  # must be implemented by every sub class
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r 
    def area(self): 
        return 3.14159*self.r**2
    def perimeter(self):
        return 2 * 3.14159 * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w 
        self.h = h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)
    

c = Circle(5)
print(c.area())
print(c.perimeter())

r = Rectangle(10, 5)
print(r.area())
print(r.perimeter())

print()

# classwork:
    # GROUP EXCERCISE  

