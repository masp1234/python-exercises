class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print('"x" is validated!')

        except ValueError:
            raise ValueError('"x" must be a number') from None
    
    @property
    def y(self):
        return self.y
    
    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print('"y" is validated!')

        except ValueError:
            raise ValueError('"y" must be a number') from None
        
point = Point(1, 'hello')