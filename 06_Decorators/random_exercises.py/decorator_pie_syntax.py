from decorators import my_decorator, do_twice


@my_decorator
# @do_twice - man kan godt have flere decorators på
def say_whee():
    print('Whee!')


say_whee()

@do_twice
def say_whee_twice():
    print('Whee!')

say_whee_twice()

@do_twice
def say_whee_with_parameters(name):
    print(f'Whee! {name}')


say_whee_with_parameters('World')

@do_twice
def return_greeting(name):
    print('Creating greeting')
    return f'Hi {name}'

print(return_greeting('bob'))

# Before using functools.wraps in decorators.py, the method returned help for the wrapper function and also printed the name of the wrapper function
help(return_greeting)
print(return_greeting.__name__)





