"""



namedtuple:
برای خواندن جزئیات، به صفحه 142 کتاب ترفند های پایتون، ترجمه بابازاده مراجعه شود

Returns a new subclass of tuple with named fields.



"""

from collections import namedtuple
# strucrure = namedtuple('ClassName', ['attr1', 'attr2'])
# strucrure = namedtuple('ClassName', 'attr1', 'attr2') attrs => split()

Car = namedtuple('Car', ['name', 'color',])


c1 = Car('benz', 'white')
print(f'__class__: {c1.__class__}')
print(f'__doc__: {c1.__doc__}')
print(f'__repr__: {c1.__repr__()}')
print(f'__str__: {c1.__str__()}')

# print(c1)
# print(*c1)

# name, color = c1
# print(color)

# helper properties
Electric = namedtuple('ElectricCar', Car._fields + ('charge',))
e1 = Electric('tesla', 'yellow', 200)
print(e1._asdict())

# Inheritance
class CarColor(Car):

    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return f'#000000'

c2 = CarColor('bmw', 'red')
print(c2.hexcolor())
