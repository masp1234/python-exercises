import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return result
    
    return wrapper

@timer
def test(num):
    for i in range(num):
        print(i)


test(10000)
    


