import random

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def students_list(num_students):
    students = []
    for i in range(num_students):
        name = random.sample(names, 1)
        major = random.sample(majors, 1)
        students.append({'id': i, 'name': name[0], 'major': major[0]})
    return students

def students_generator(num_students):
    
    for i in range(num_students):
        name = random.sample(names, 1)
        major = random.sample(majors, 1)
        yield {'id': i, 'name': name[0], 'major': major[0]}

for student in students_generator(20):
    print(student)