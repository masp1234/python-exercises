
# List comprehension
squares = [x * x for x in range(10)]



# Set comprehension
# ser lidt underligt ud, men det er jo fordi der kun kan være unikke værdier i et Set

set = { x * x for x in range(-9, 10) }
print(set)

# Dict comprehension
dict = { x: x * x for x in range(5) }
print(dict)

