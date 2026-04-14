# classes :
# person- base class
# student - has name , age, grades; can claculate average_grades() and check is_passing()
# Teacher - has name, subject, salary, can give_raise(percent).
# school - manages lists of students and teachers, methods: enroll() and hire().
# polymorpism - introduces() behaves diffrently for student as teache.
# cli menu - user can email students, hire teachers, view all people and check a student grade


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'Hi i am {self.name} and i am {self.age} years old')
    

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.grade_list = []
    
    def average_grade(self):
        return sum(self.grade_list) / len(self.grade_list) if self.grade_list else 0
        
    def is_passing(self, passing_score = 50):
        passing = self.average_grade() >= passing_score
        return passing
    
    def introduce(self):
        return f'i am {self.name} and i am a student, average grade is {self.average_grade():.1f}'

class Teacher(Person):
    def __init__(self, name,age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def give_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
    
    def introduce(self):
        return f'i am {self.name} and i teach {self.subject}'
    

class School():
    def __init__(self, name):
        self.name = name
        self.student = []
        self.teacher = []
    
    def enroll(self, student):
        self.student.append(student)
        print()
        print('Student successfuly enrolled!!')

    def hire(self, teacher):
        self.teacher.append(teacher)
        print(f'{self.name} is succesfully hired')

    def view_all(self):
        print(f'-----------{self.name} directory------------')
        print('---teachers:\n')
        for x in self.teacher:
            print(f'- {x.introduce()}')
        print('\n----students:')
        for x in self.student:
            print(f'- {x.introduce()}')


print()

def main():
    myschool = School('Torilo academy')
    while True:
        print('----------welcome to the school app------------')
        print('\n1.Enroll Students\n2.Hire Teachers\n3.View All\n4.Check Stdent Grade\n5.Quit')
        print()
        option = input('Enter an option: ')

        if option == '1' :
            name = input('Enter name: ')
            age = input('Enter age: ')
            new_student = Student(name, age)
            grades = input('Enter grades (seprated by spaces): ')
            if grades:
                new_student.grade_list = [float(x) for x in grades.split()]
            myschool.enroll(new_student)

        elif option == '2':
            name = input('Enter nane: ')
            age = int(input('Enter age: '))
            subject = input('Enter subject: ')
            salary = float(input('Enter salary: '))
            myschool.hire(Teacher(name, age, subject, salary))

        elif option == '3':
            myschool.view_all()

        elif option == '4':
            student_name = input('Student name: ')
            student = next((x for x in myschool.student if x.name.lower() == student_name.lower()), None)
            if student:
                status = 'passing' if student.is_passing() else 'fail'
                print(f'{student.name} - Average: {student.average_grade():.1f} ({status})')
            else:
                print('Student not found')

        elif option == '5':
            break

if __name__ == '__main__':
    main()




print()
    


