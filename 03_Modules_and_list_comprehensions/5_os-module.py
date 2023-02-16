import os

# 5.1 create a folder and name the folder 'os_exercises'.
if os.path.exists('/Users/masp9/python/python-classes/03_Modules_and_list_comprehensions/os_exercises'):
    print('Folder already exists')
else:
    os.mkdir('os_exercises')

# 5.2 In that folder create a file. Name the file 'exercise.py'
file = open('os_exercises/exercises.py', 'w')

# 5.3 get input from the console and write it to the file.
file.write(input())

# 5.4 repeat step 2 and 3 (name the file something else).
file2 = open('os_exercises/something-else.py', 'w')
file2.write(input())

# 5.5 read the content of the files and and print it to the console.
file = open('os_exercises/exercises.py', 'r')
file2 = open('os_exercises/something-else.py', 'r')

print(file.read(), file2.read())


