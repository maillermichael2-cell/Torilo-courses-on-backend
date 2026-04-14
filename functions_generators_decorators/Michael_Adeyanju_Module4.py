# TASK 1 
# calculate area
print('||| TASK 1 ')
print('||| 1A. CALCULATE AREA')
pi = 3.14
coefficient = 0.5
def calculate_area(shape, *dims):
    if shape == 'circle':
        radius = dims[0]
        area = pi * radius**2
        area_return1 = f'Area of a circle given the radius of {radius} = {area}'
        return area_return1

    if shape == 'rectangle':
        length = dims[0]
        width = dims[1]
        area = length * width
        area_return2 = f'Area of a rectangle given the length {length} and width {width} = {area} square units'
        return area_return2
    
    if shape == 'triangle':
        base = dims[0]
        height = dims[1]
        area = coefficient * base * height
        area_return3 = f'Area of a triangle given the base {base} and height {height} = {area} square units'
        return area_return3

circle = calculate_area('circle', 100)
print(circle)
rectangle = calculate_area('rectangle', 200, 100)
print(rectangle)
triangle = calculate_area('triangle', 100, 250)
print(triangle)
print()



# # is palindrome
print('||| 1B. IS PALINDROME')
def is_palindrome(word):
    side = word[::-1]
    if side == word[::1] :
        print(f'True the word {word} is a palindrome')
    else :
        print(f'False')

is_palindrome('civic')
print()

# celcius to fanrenheit
print('||| 1C. CONVERT CELCIUS TO FANRENHEIT')
def celcius_to_fanrenheit(c):
    fan = c * 2 + 30
    return f'converting {c} degrees celsius to fanrenheit is {fan} degrees fanrenheit'

ret = celcius_to_fanrenheit(200)
print(ret)
print()


# count_words
print('||| 1D. COUNT WORDS')
def count_words(sentence):
    words = sentence.split()
    count = len(words)
    return_count = f'Count for the words in the function: {count} words'
    return return_count

sentence = count_words('Good evening michael its nice to meet you')
print(sentence)
print()

# the most frequent item in a list 
print('||| 1E. MOST FREQUENT IN THE LIST ')

data = [1,2,3,3,4,5,6,7,8,9,10]

def most_frequent(lst):
    mode = max(set(lst), key=lst.count)
    return_mode = f'the most frequent number in the list is {mode}'
    return return_mode

ret = most_frequent(data)
print(ret)
print()


# TASK 2 FIBONACCI SEQUENCE
print('||| 2. FIBONACCI SEQUENCE')
def fibonacci_generator(x):
    a, b = 0, 1
    for n in range(x):
        yield a
        a, b = b, a + b

fib = fibonacci_generator(10)
lst = fibonacci_generator(10)
fib_in_list = list(lst)
print('generator: ')
for x in fib:
    print(x, end='')
print('\n')
# list approach
return_fib = f'fibonacci sequence to N terms = {fib_in_list}'
print(return_fib)
print()


# TASK 3 TIMIMG DECORATOR
print('||| 3. TIMING DECORATOR')
def timer(func):
    def wrapper():
        print('Starting...')
        result = func()
        print('end...')
        if result == 999999:
            one_sec = 1000000 # using 1 milllion micro seconds to define actual time
            adjust_time = result / one_sec
            sec = adjust_time / 60
            print(f'used {sec:.2f} sec of computer time for the loop function ')
        else :
            print('none')
    return wrapper
    
@timer
def loop():
    for x in range(1000000):
        pass
        if x == 1000000:
            break
    return x
loop()

print()
# TASK 4 USER PROFILE WITH **KWARGS
print('||| 4. USER PROFILE ')
def user_profile(**kwargs):
    return kwargs

user1 = user_profile(name="mike", age="25", city="Lagos", course="backend", year_started="2026")
ret = list(user1.values())
print(f'My name is {ret[0]} and i am {ret[1]} i live in the city of {ret[2]} and i am studying {ret[3]} in the year {ret[4]}')
print()