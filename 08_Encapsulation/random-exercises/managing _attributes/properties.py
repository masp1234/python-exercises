class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print('Get radius')
        return self._radius
    
    def _set_radius(self, radius):
        print('Set radius')
        if radius < 0:
            # raise ValueError('The radius cannot be below 0.')
            print('The radius cannot be below 0.')
            return
        self._radius = radius

    def _del_radius(self):
        print('Delete radius')
        del self._radius

   # Using keyword arguments to avoid confusion and be sure you assign the correct things 
    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property"
    )

circle = Circle(5)
print(dir(circle.radius))
print(circle.radius)
circle.radius = -1
print(circle.radius)
circle.radius = 10
print(circle.radius)

""" del circle.radius
print(circle.radius) """



    