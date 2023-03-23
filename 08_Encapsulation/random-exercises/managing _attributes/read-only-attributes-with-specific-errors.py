class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        raise AttributeError('"x" is read-only')
    
    @x.deleter
    def x(self):
        raise AttributeError('"x" is read-only')
    
    @property
    def y(self):
        return self._y


point = Point(2, 10)
print(point.x)
point.x = 10