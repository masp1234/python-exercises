from contextlib import contextmanager

# does the same as the class below the contextmanager matches the finally block to exit and enter to whatever happens before that
# the @contextmanager decorator needs a generator function to work
@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()



# wont work if its lowercase, since it will override the normal open class, which is supposed to be called on line 9
class Open:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        print('__enter__')
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        print('__exit__')
        print(f'{type}, {value}, {traceback}')
        self.file.close()
        if type == FileNotFoundError:
            return True

# Context manager - 'with' looks for an __enter__ and __exit__ method, and 'as file' is the value returned by enter
with Open('test.tfxt', 'r') as file:
    print(file.readline())



