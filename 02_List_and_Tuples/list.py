courses = ['History', 'Math', 'Physics', 'Compi Sci']

# Returnerer en ny liste
print(sorted(courses, key=len, reverse=True))

courses.append('Art')
print(courses)

# Indsætter et array på index 2
courses.insert(2, ['Hello', 'Test'])
print(courses)
