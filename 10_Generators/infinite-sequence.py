# Finite sequence
a = range(5)
print(list(a))

# Infinite sequence
def infinite_sequence():
    num = 0
    while True:
        yield num
        if num == 10000:
            break
        num += 1

for number in infinite_sequence():
    print(number)

# You can also call next() on the generator object manually. Good for sanity checking
gen = infinite_sequence()
print(next(gen))
print(next(gen))