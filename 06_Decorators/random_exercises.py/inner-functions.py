
# trying to call first_child() outside the parent function gives an error, since it does not exist outside the parent function
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

parent()

# Note that it is a reference to the function that is returned, not a call to the function
def parent2(num):
    def first_child():
        return 'Hi, I am Emma'
    
    def second_child():
        return 'Call me Liam'
    
    if num == 1:
        return first_child
    else:
        return second_child
    

first_child = parent2(1)
second_child = parent2(1000)

# Prints a reference to the function, since it is not called
print(first_child)
# Is called
print(second_child())
    
