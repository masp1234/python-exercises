class PythonStudents:

    def __init__(self):
           self.students = [Student("name1", 1234), Student("name2", 4321), Student("name3", 9876)]

    def __iter__(self):
           self.current_index = 0
           return self
    
    def __next__(self):
           if self.current_index == len(self.students):
                  raise StopIteration
           current_student = self.students[self.current_index]
           self.current_index += 1
           return current_student.name
           




class Student:

     def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

     @property
     def name(self):
             return self.__name

     @name.setter
     def name(self, name):
             self.__name = name.capitalize()

     def __add__(self, student):
             return Student('Anna the daugther', 1234)

     def __str__(self):
             return f'{self.name}, {self.cpr}'

     def __repr__(self):
             return f'{self.__dict__}'

students = PythonStudents()
#iter = iter(students)
#print(next(iter))
#print(next(iter))
#print(next(iter))
#print(next(iter))

for student in students:
       print(student)


# could also write
for student in PythonStudents():
       print(student)