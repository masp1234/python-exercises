import functools
import time

def my_decorator(func):
    def wrapper():
        print('Something is happening before the function is called')
        func()
        print('Something is happening after the function is called')
    return wrapper

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

def timer(func):
    # Print the runtime of the decorated function
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter() # 2
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} secs')
        return value
    return wrapper_timer

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

def slow_down(func):
    # Sleep 1 second before calling the function
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        print(args, kwargs)
        time.sleep(args[1])
        return func(*args, **kwargs)
    return wrapper_slow_down
        

