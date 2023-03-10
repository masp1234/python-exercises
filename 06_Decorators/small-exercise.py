import time

def log(func):
    def wrapper(*args):
        file = open('small-exercise-log.txt', 'a')
        x = func(*args)
        file.write(f'Result: {x}, timestamp: {str(time.ctime())}, arguments: {args}\n')
        return x
    return wrapper

@log
def add(*args):
    return sum(args)

@log
def printer(x):
    return f'this is printed {x}'

"""
# instead of using the pie-notation you could do these
add = log(add)

# or

wrappedFunction = log(add)
"""


print(add(1, 2, 3, 4))
print(printer('hello'))

