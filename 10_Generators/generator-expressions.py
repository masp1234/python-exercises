# Also called Generator comprehensions

import sys
# Size is 85176 bytes
# returns a full list
nums_squared_list_comprehension = [num ** 2 for num in range(10000)]
print(sys.getsizeof(nums_squared_list_comprehension))

# prints the list
print(nums_squared_list_comprehension)

# Size is 208 bytes, no matter the size, since it only returns the generator
# returns a generator
# Using a generator function or generator expression/comprehension is the same
nums_squared_generator_comprehension = (num ** 2 for num in range(10000))
print(sys.getsizeof(nums_squared_generator_comprehension))

# prints the memory address of the generator object
print(nums_squared_generator_comprehension)