from time import sleep
# instead of doing this, where you have to wait for all the elements in the list
def compute():
    list = []
    for i in range(10):
        sleep(.5)
        list.append(i)
    return list

print(list)

# iterator class
class Compute:
    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        self.start += 1
        if self.start > 10:
            raise StopIteration
        return self.start
    
# generator function
def compute():
    for i in range(10):
        yield i


generator = (i for i in range(10))