from sqlite3 import connect
from contextlib import contextmanager
from student import Student

""" with connect('testfiles/school.db') as conn:
    # creating a cursor object - read about cursor ????
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS students(id int PRIMARY KEY, name text, cpr text)')
    cur.execute('INSERT INTO students(id, name, cpr) VALUES (1, "Claus", "223344-5566")')
    cur.execute('INSERT INTO students(id, name, cpr) VALUES (2, "Julie", "111111-1111")')
    cur.execute('INSERT INTO students(id, name, cpr) VALUES (3, "Hannah", "222222-2222")')

    for i in cur.execute('SELECT * FROM students'):
        print(i)
    
    cur.execute('DROP TABLE students')
 """
    
@contextmanager
def write_to_db(path):
        connection = connect(path)
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS students(id int PRIMARY KEY, name text, cpr text)')
        yield connection

        cursor.execute('DROP TABLE students')
        connection.close()


students = [Student(1, 'Bob', 'CPR123'), Student(2, 'B', 'CPR123'), Student(3, 'C', 'CPR123')]

with write_to_db('./testfiles/schoo.db') as connection:
    cursor = connection.cursor()
    for student in students:
            cursor.execute(f'INSERT INTO students(id, name, cpr) VALUES ({student.id}, "{student.name}", "{student.cpr}")')
    
    for i in cursor.execute('SELECT * FROM students'):
        print(i)
