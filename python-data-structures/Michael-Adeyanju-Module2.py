# assignment2 

# students lists
students = [
    {"id":1, "name":"mike","age":30,"score":150,"passed":True,"city":"lagos"},
    {"id":2, "name":"chris","age":15,"score":100,"passed":False,"city":"ogun"},
    {"id":3, "name":"kunle","age":35,"score":50,"passed":True,"city":'osun'},
    {"id":4, "name":"lanre","age":40,"score":70,"passed":False,"city":"abia"},
    {"id":5, "name":"tobi","age":80,"score":110,"passed":True,"city":"adamawa"},
]

#students who passed 
for x in students :
    if x['passed'] == True :
        print('STUDENTS WHO PASSED : ')
        print(f'NAME: {x['name']}')
        

# students that has the highest score using max()
highest_score = max(x['score'] for x in students)
print(f'|| HIGHEST SCORE: {highest_score}')


# creating a set of all unique cities in student records
unique_cities = {x["city"] for x in students}
unique_cities_in_set = set(unique_cities)
print(f"Cities: {unique_cities_in_set}")

#add a new student
new_student = {"id":6,"name":"kike","age":45,"score":20,"passed":False,"city":"lagos"}
students.append(new_student)
print('NEW STUDENTS ADDED : ')
print(students)

#delete student by name
name_to_delete = "chris"

for i in range(len(students)):
    if students[i]["name"] == name_to_delete:
        deleted_student = students.pop(i)
        print(f"DELETED STUDENT NAME: {deleted_student['name']}")
        print(students)
        break


