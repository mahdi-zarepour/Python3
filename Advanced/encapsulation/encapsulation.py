"""


encapsulation: getter-setter-deleter
کپسوله سازی در پایتون به این معنی است که اجازه دسترسی مستقیم به اتربیوت رو ندیم و در عوض با استفاده از متدهای 
setter, getter, deleter, 
این کار رو انجام میدیم
این کار باعث می شود اتربیوت های حساس ما به راحتی تغییر نکند


روش استفاده در پایتون:
در داندر اینیت ما مقداری رو دریافت نمی کنیم و فقط میایم دستی دیفالتش رو ست می کنیم



"""

class Person:

    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
            
    @age.deleter
    def age(self):
        self.__age = 0

person_1 = Person()
person_1.age = 18 # setter
person_1.age # getter
del person_1.age # deleter