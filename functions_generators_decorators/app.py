# MODULE4 : functions generators and decorators

# GENERATORS: is a special type of iterable that is used to 
# way tp create a genertor 

# 1. using generator functions (yield) to produce a sequence of values in a raising manner
# def count_up_to_ten(x):
#     count = 1 
#     while count <= x :
#         yield count # used for generator functions : it produces a sequence of values 
#         count += 1 
# counter = count_up_to_ten(10)
# for num in counter :
#     print(num)

# 2. using generator expressions is similar to list comprehension we use parenthessis in generator expresion
# squares = (x**2 for x in range(10) if x % 2 == 0)
# # using the generator
# for squares in squares:
#     print(squares) 

# DECORATORS : is a function that modifyies the function of another function 
# example of a decorator without using the @ symbol :
# def great_decorator(func):
#     def wrapper():
#         print('Hello!')
#         func()
#         print('Good bye')
#     return wrapper

# def say_name():
#     print('My name is Python.')


# decorate = great_decorator(say_name)
# decorate()

# using the @ symbol 
# def great_decorator(func):
#     def wrapper():
#         print('Hello')
#         func()
#         print('Goodbye!!')
#     return wrapper

# @great_decorator
# def say_name():
#     print('my name is victoria')

# say_name()
# parameters are vairables we define in a function arguments are values that we put when calling the function 

# EXAMPLE OF A DECORATOR WITH ARGUMENTS 
# def great_decorator(func):
#     def wrapper(*args,**kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper
# @great_decorator
# def add(a, b):
#     print(f'Adding: {a} + {b}')
#     res = a + b
#     print(f'Total: {res}')

# add(5,3)

# functions is a block of reusable code that alows ypu to perfom a task
# def greet(name):
#     return f'hello  {name}'

# name = greet('michael')
# print(name)

# def add(a,b):
#     return f'Addition : {a + b}'

# print(add(2,3))

# def square(x):
#     return f'Squares {x * x}'

# print(square(5))

# types of functions
# built in functions print(), len(), input(), type()
# user defines functions functions written by your self eg greet()
# lambda anonymous functions short functions with no name, they are used for simple operations eg square = lambda x: x * x print(square(5))

# functions with default arguments
# def add(val=2):
#     return f'result : {2 * val}'

# print(add())

# def divide(a,b):
#     return a / b
# print(divide(10,2))

# functions with variables - lenght arguments 
# * args - multiple positional arguments
# **kwargs - multiple keyword arguments

# def print_args(*args):
#     for x in args:
#         print(x)
# print_args(1,2,3)


# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
# data = print_kwargs(name='john', age='30')
# print(data)


# scope of variables in and outside functions
# x = 10  # global scope because its defined outside the function
# def show():
#     x = 5 # local scope because its defined inside the function
#     print(x) # local scope printing 

# show()        # calling the function
# print(x)    # global scope printing

# classwork 1 
# write a function with *args that sums any number of values 
# write a decorator that prints function started and function ended around any function

# class work 1 
# def add(*args):
#     return sum(args)

# print(f'Total : {add(2,5,6)}')

# class work 2 
# def decorator(func):
#     def wrapper():
#         print('Function started')
#         func()
#         print('function ended')
#     return wrapper
# @decorator
# def greet():
#     print(f'Good afternoon Michael')
# greet()

# def req():
#     data = input('whats your name : ')
#     print(f'my name is {data}')
# req()

    





