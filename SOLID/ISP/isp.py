"""

Interface Segragation Principle:
many client-specific interfaces are better than one general-purpose interface
بجای ایجاد یک کلاس بزرگ و پایه که چندین کار رو انجام می دهد و بقیه کلاس ها قرار است از آن ارث بری کند، تبدیل
به چندین کلاس کوچک تر کنید. شبیه به اصل اول است

"""
from abc import ABC, abstractmethod


# no ISP
# class Shape:
#     def circle(self):
#         pass

#     def square(self):
#         pass
    
#     def rectangle(self):
#         pass


# class Circle(Shape):
#     def circle(self):
#         print('one circle')

#     def square(self):
#         pass
    
#     def rectangle(self):
#         pass


# class Square(Shape):
#     def circle(self):
#         pass

#     def square(self):
#         print('one square')
    
#     def rectangle(self):
#         pass


# -------------

# ISP
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print('Circle')


class Square(Shape):
    def draw(self):
        print('Square')