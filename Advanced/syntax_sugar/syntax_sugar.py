"""



Synatx Suger:
    __getitem__, __setitem__, __delitem__

ما برای زیبایی و سینتکس راحت تر از این متود استفاده می کنیم و این متود ها به خودی خوددر عمل کار خاصی
را انجام نمی دهند اما می توانند نحوه نگارش کد را بهتر کنند. این متود ها به سینتکس سوگر مشهورند

Custom Methods:
اگر بخواهیم با آیتم ها درون کلاس کار کنیم، از نحوه اول استفاده می کنیم. این متود ها بصورت کاستوم است و 
بهم ریختگی زیادی در کد وجود می آورد. اما پایتون این متود ها را فراهم کرده است تا کار را زیباتر و راحت کند


Syntax Suger:
اگر بخواهیم با استفاده مستقیم از آبجکت و
استفاده از ایندکس این عملیات ها انجام شود، از این سه متود استفاده می کنیم. مثال:
mylist[3] => __getitem__
my_list[3] = 4 => __setitem__
del my_list[3] => __delitem__



"""

# Custom Methods
# class MyList:
    
#     def __init__(self, element=1):
#         self.my_list = [None] * element

#     def __str__(self):
#         return str(self.my_list)
    
#     def __repr__(self):
#         return f'{self.__class__.__name__}({self.my_list})'

#     def set_item(self, key, value):
#         self.my_list[key] = value
    
#     def get_item(self, key):
#         return self.my_list[key]

#     def del_item(self, key):
#         self.my_list[key] = None


# a = MyList(5)
# a.set_item(0, 00)
# a.set_item(1, 11)
# a.set_item(2, 22)
# a.set_item(3, 33)
# a.set_item(4, 44)
# a.del_item(1)
# print(a.get_item(1))
# print(a)


# -------------
# Syntax Suger
class MyList:

    def __init__(self, element=1):
        self.my_list = [None] * element

    def __str__(self):
        return str(self.my_list)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.my_list})'

    def __setitem__(self, key, value):
        self.my_list[key] = value
    
    def __getitem__(self, key):
        return self.my_list[key]

    def __delitem__(self, key):
        self.my_list[key] = None


my_list = MyList(5)
my_list[0] = 00
my_list[1] = 11
my_list[2] = 22
my_list[3] = 33
my_list[4] = 44
del my_list[1]
print(my_list[2])