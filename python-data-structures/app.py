# # # class 2 of python class


# # # 1. lists: store multiple items in a single vairable it can be orderd and changable

# # #  fruits = [
# # #      "mango","apple","orange"
# # # ]
# # # modifying : we can change the values in a list based on their index
# # # fruits[1] = "banana"
# # # print(fruits[1])
# # # add another to the list
# # # fruits.append('cherry')
# # # print(fruits)
# # # remove 
# # # fruits.remove('cherry')
# # # print(fruits)


# # # 2. TUPLES: TUPLES CANT BE CHANGED 
# # #  cordinates = (
# # #      '20.3','18.9'
# # #  )
# # #  print(cordinates[0])
# # #  #modify we cant change or reassign data in tuples


# # # 3. SETS : UNIQUE UNORDERD ITEMS DATA IN IT ARE NOT ORDERD THET CHANGE POSITIONS
# # # colors = {'red','green','yellow','orange'}
# # # #add to set
# # # colors.add('black')
# # # print(colors)
# # # #remove from set 
# # # colors.discard('black')
# # # print(colors)

# # # EXAMPLE2: SETS DOSENT ALLOW DUPLICATES OV DATA EG IT CANT ALLOW 1,2,2,3 OUTPUT 1,2,3
# # # numbers = {1,2,2,3}
# # # print(numbers)

# # # 4. DICTIONARIES : STORE KEY VALUE PAIRS

# # # person = {
# # #     "name": "michael",
# # #     "age": 25,
# # #     "city": "Lagos State"
# # # } 
# # # # access a specific data
# # # print(person["name"])

# # #add 
# # # person.update({"email":"mike"})
# # # print(person)
# # # # correct way 
# # # person['email'] = 'kunle@gmail.com'
# # # print(person)
# # # # remove 
# # # # person.pop('age')
# # # # print(person)
# # # # python way of removing data
# # # del person["age"]
# # # print(person)

# # #METHODS FOR DICTIONARIES
# # # print(person.keys()) keys() this displayes the keys of the data base
# # # print(person.values()) values shows the values of the database
# # # print(person.items()) item prints the data line by line 

# # # RANGE : USED TO GENERATE A SEQUENCE OF NUMBERS ESPECIALLY IN LOOPS range(start, stop, step)
# # # numbers = range(0, 11, 3) # to present this we use a loop

# # # for x in numbers: # use cases 
# # #     print(x)

# # # classwork 1
# # # book = {
# # #     "title": "Things fall apart",
# # #     "author": "chinachebe",
# # #     "price": 18.50,
# # #     "available": False
# # # }
# # # print(book)

# # # class work 2
# # students = [
# #     {"id":1, "name": "michael","age":23, "course": "backend"},
# #     {"id":2, "name": "chris","age":20, "course":"ai enginerring"},
# #     {"id":3, "name": "governor", "age":"30", "course": "full stack"}
# # ]
# # id = 1
# # for x in students:
# #     if students['id'] == id :
# #         print(f'ID: {x[0]['id']}')
# #         print(f'NAME: {x[0]['name']}')
# #         print(f'AGE: {x[0]['age']}')
# #         print(f'COURSE: {x[0]['course']}')
        

# # # print(f'ID: {x['id']} NAME: {x['name']} Age: {x['age']} COURSE: {x['course']}')

# # # class work 3
# # my_list = [1,2,2,3,4,4,5]
# # #set
# # set_cont = set(my_list)
# # list_cont = list(set_cont)
# # print(list_cont)

# data = [
#     {"id":1,"name":"michael","age":25,"money":23000,"status":"rich"},
#     {"id":2,"name":"anjela","age":20,"money":19000,"status":"business"},
#     {"id":3,"name":"pat","age":19,"money":10000,"status":"poor"}
# ]

# crs = {x["money"] for x in data}
# calc = max(crs)
# print(calc)


# # this is for accessing just one key in the list of dictionaries
# age = {x['age'] for x in data}
# print(set(age))

# # this is for accessing all the data in the list of dictionaries
# for x in data :
#     if x['status'] == 'poor':
#         print(x['name'])

# status = [x['status'] for x in data]
# print(status)
# status_in_set = set(status)
# print(status_in_set)





# # # WHEN DO YOU USE ALL THE DATA TYPES 
# # # lists = general collections
# # # tuple = fixed and constant data 
# # # sets = unique items , membership
# # # dict = key value relationship


data = [
    {"id":1, "name":'mike',"age":20},
    {"id":2, "name":'chike',"age":60},
    {"id":3, "name":'bayo',"age":30}
]

# data_query = [x['name'] for x in data]
# print(set(data_query))

# age_diff = [x['age'] for x in data]
# print(max(age_diff))

agee = 60
for x in range(len(data)) :
    print(data[x]['name'])
    print(data[x]['age'])
    print(data[x]['id'])
    if data[x]['age'] == agee :
        delete = data.pop(x)
        print(data)
        break

