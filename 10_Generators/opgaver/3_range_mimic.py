class range_mimic():

    # step = 1 as default value
    def __init__(self, start_index, stop_index, step=1):
        # calling the object itself and invoking the '__call__' dunder method
        self(start_index, stop_index, step)
    
    # initializes the list with the given parameters
    def __call__(self, start_index, stop_index, step):
        current_index = start_index
        list = []
        while current_index < stop_index:
            list.append(current_index)
            current_index += step
        self._values = list
    
    def __iter__(self):
        self._current_index = 0
        return self
    
    def __next__(self):
        if self._current_index >= len(self._values):
            raise StopIteration
        
        current_element = self._values[self._current_index]
        self._current_index += 1

        return current_element



print('r 1')
r = range_mimic(1, 10, 2)
for i in r:
    print(i)

print()

print('r 2')
r2 = range_mimic(1, 11)
for i in r2:
    print(i)

print()

print('r 3')
r3 = range_mimic(-20, 45, 4)
for i in r3:
    print(i)