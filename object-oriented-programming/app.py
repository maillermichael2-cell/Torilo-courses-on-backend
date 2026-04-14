# object oriented programming 

# classes, objects, methods and encapsulation

# OOB ORGANIZES CODE AROUND OBJECTS ITS IMPORTANT IN DJANGO 
# whats oob 
# 
# CLASSES : IS A BLUE PRINT 
# OBJECT IS AN INSTANT CREATED FROM THE CLASS
# 
# EXAMPLE ON SELF AND __INIT__:
# to define a class 
# class person:
#     # consturctir that runs when a new object is created 
#     def __init__(self, name, age):
#         # store the name in the object 
#         self.name = name # instance vairable
#         self.age = age # instance vairable
#     # this is a method to display a greeting 
#     def greet(self):
#         print(f'Hello my name is {self.name} and i am {self.age} years old.')
#     # this is a method to increase age by 1 
#     def birthday(self):
#         self.age += 1 
#         print(f'Happy birthday {self.name}! Now {self.age}.')

# # create object (instances)
# ayo = person('ayo', 25)
# kemi = person('kemi', 35)

# # call methods 
# ayo.greet()
# ayo.birthday()
# kemi.greet()

# # access attributes directly 
# print(ayo.name)
# print(ayo.age)

# NOTE : VERCEL FOR FRONTEND RENDER FOR BACKEND USE YOUR GITHUB ACCOUNT TO LOGIN TO REBDER 
# instance vairable belongs to each individual 
# object class variable are sheard between all instance of the class
# class Student:
#     school = 'Torilo academy' # class vairable 
#     # constructor
#     def __init__(self, name, score): # this is to initalize
#         self.name = name # instance vairable - unique per object
#         self.score = score  # instance vairable 

# s1 = Student('bayo', 45)
# s2 = Student('tolu', 25)

# print(f's1 student info : {s1.name} score: {s1.score} in the school : {s1.school}')
# print(f's2 student info : {s2.name} score" {s2.score} in the school : {s1.school}')

# # changing the class vairable affects all instances 
# Student.school = 'New Academy'
# print(s1.school)
# print(s2.school)

# # printing new info since we have changed all instances 
# print(f's1 student info : {s1.name} score: {s1.score} in the school : {s1.school}')
# print(f's2 student info : {s2.name} score" {s2.score} in the school : {s1.school}')


# class BankAccount:
#     interest_rate = 0.05 # class vairable 
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self._balance = balance # private -___prefix


#     # instance method - operates on self
#     def deposit(self,amount):
#         self._balance += amount
#         print(f'Deposited {amount}. Balance {self._balance}')

#     def withdraw(self, amount):
#         if amount > self._balance:
#             print('insufficient funds.')
#         else :
#             self._balance -= amount

#     def get_balance(self):
#         return self._balance  # getter for private attribute
    
#     # class method - operates on the class
#     @classmethod
#     def set_rate(cls, rate):
#         cls.interest_rate = rate
#     # static method - utility, no access to class/instance
#     @staticmethod
#     def validate_amount(amount):
#         return amount > 0
    
# (
# 
# library_code.search_by_author('kunle')
# list_of_books = library_code.list_of_books()
# library_code.total_of_books()
# library_code.validate("inter")


# member = Member("mikol0")
# member.borrow(library_code, 'inter')
# member.return_book(library_code, 'inter')
# )
# # usage 
# acc = BankAccount('mike', 2000)
# acc.deposit(500)
# acc.withdraw(200)
# print(f'New balance : {acc.get_balance()}')
# BankAccount.set_rate(0.07)
# print(BankAccount.validate_amount(100))

# encapsulation means bundling data and the meothod that operates on it inside one class and restrictin direct access to same of that data
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#         # getter - controlled read access
#     def get_salary(self):
#         return self.__salary
#         # setter - controlled write access with validation
#     def set_salary(self, amount):
#         if amount < 0 :
#             print('Salary cannot be negative.')
#         else :
#             self.__salary = amount

# emp = Employee('mike', 6000000) 
# emp2 = 
# print(emp.get_salary())
# print(f'{emp.name} salary is : {emp.get_salary()}')

# CLASS WORK
# a simple bank account 
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance

user1 = BankAccount(1000)
user1.deposit(500)
print(f'Available new balance : {user1.get_balance()}')

# class work 2 : 


# POLYMORPISIM: 



        