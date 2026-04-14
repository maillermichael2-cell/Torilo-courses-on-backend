# a conditional is used to make descisions in a program based on wheater the condition is true or false 

# if statement
# age = 18

# if age >= 18 :
#     print('you are an adult!!!')
# elif age > 12 :
#     print('you are a teenager!!!')
# else :
#     print('you are a child!')


# for loop is used to iterate over a sequence of list, range
# this is a for loop
# for x in range(100,10,-10):
#     print('number:', x)

# for while loop runs as long as a condition is true
# count = 0
# while count < 3 :
#     print('Count is:', count)
#     count += 1


# exceptions : 
# try : 
#     number = int(input('Enter a number: '))
#     print(10 / number)
# except ZeroDivisionError:
#     print('Cannot divide by zero')
# except ValueError:
#     print('Please enter a valid number.')
# except Exception as e:
#     print('An error occured: ', e)

# list comprehension
# squares = [x**3 for x in range(6)]
# print(squares)

# evens = [x for x in range(10) if x % 2 == 0] 
# print(evens)

# odd = [x for x in range(10) if x % 2 == 1] 
# print(odd)

# labels = ['Even' if x % 2 == 0 else 'Odd' for x in range(5)]
# print(labels)


# # NETSED LIST COMPREHENSION
# 2 x 2 multiplication table 

# table = [[(i+2) * (j+2) for j in range(5) ] for i in range(5)]

# for row in table :
#     print(row)

# write a loop that count down from 10 and prints blast off

# message = 'blast off !!!'
# for x in range(10, 0, -1):
#     print(x)
#     if x == 1 :
#         print(message)

# 
# data = [
#     {"id":1, "name": "Mcvities Biscuit", "price": 12000},
#     {"id":2, "name": "orijin bitters", "price": 1000},
#     {"id":3, "name": "action bitters", "price": 2000},
#     {"id":4, "name": "chealse sachet", "price": 800},
#     {"id":5, "name": "agege bread", "price": 1200}
# ]

# total = [x['price'] for x in data]

# total_price = sum(total)
# print(f'Total Price: {total_price}')

# classwork 3 : use list comprehension to filter even numbers from 1 - 20

# evens = [x for x in range(1,21) if x % 2 == 0]
# print(evens)


# num = int(input("Input number: "))
# table = [[(i+num) * (j+1) for j in range(2) ] for i in range(12)]
# for x in table:
#     print(x)

# Get the number from the user
num = int(input("Enter a number to see its multiplication table: "))

x = 1

print(f"Multiplication Table for {num}:")

# Use a while loop to go from 1 to 12
while x <= 12:
    result = num * x
    print(f"{num} x {x} = {result}")
    i += 1  # Increment the counter to avoid an infinite loop


data = [
    {"id":1, "data": 'hey whats up!!'},
    {"id":2, "data": 'how can i hlep you today?'},
    {"id":3, "data": 'wed dev is about'},
    {"id":4, "data": 'data 3 !!'},
    {"id":5, "data": 'data 4!!'},
    {"id":6, "data": 'data 5 !!'},
]
interator = [x for x in data]



