from decorators import timer, debug, slow_down

@timer
def waste_some_time(num_times):

    # ???? noget med summen af den liste som bliver lavet med list comprehension
    for _ in range(num_times):
        print(sum([i**2 for i in range(10000)]))

waste_some_time(20)


@debug
def make_greeting(name, name2, nam3, age=None):
    if age is None:
        return f'Howdy {name}'
    else:
        return f'Whoa {name}! {age} already, you are growing up!'
    

make_greeting('bob', 'dude', 'hello', 4)


# Recursive function
@slow_down
def countdown(from_number, limitRate):
    if from_number < 1:
        print('Liftoff!')
    else:
        print(from_number)
        countdown(from_number - 1, limitRate)

countdown(10, 5)