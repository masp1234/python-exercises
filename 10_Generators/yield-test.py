def yield_test():
    # if while true was not there, it would crash with a StopIteration exception
    while True:
        yield 1

print('yield_test 1')
generator = yield_test()

print(next(generator))
print(next(generator))

def yield_test2():
    print('hello')
    yield 1
    print('hello 2')
    yield 2
    
print('yield_test 2')
generator2 = yield_test2()

print(next(generator2))
print(next(generator2))