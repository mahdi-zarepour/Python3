"""



در زمان کار با کلاس های پایتون سه نوع متد وجود دارد که میتوانید از آنها استفاده کنید:

instance methods:
در پایتون 'اینستنس متود' به متدهای عادی گفته میشود که در کلاس‌ها وجود دارند و خود آبجکت رو می گیرند
به این متود ها، ریگولار(regular method) هم می گویند

class methods:
برخلاف 'اسنستنس متود' ها که آبجکت را به عنوان اولین آرگومان میگرفتند، 'کلاس متود' ها خود کلاس را به عنوان اولین آرگومان‌ میگیرند
برای ایجاد کردن 'کلاس متود' باید از دکوراتور 'کلاس متود' استفاده کنید
در زمان ساخت 'کلاس متود' دیگر نیازی به 'سلف' به عنوان اولین آرگومان ندارید و از 'سی ال اس' استفاده میکنید که اشاره به خود کلاس دارد
example:
در مثالی که در کد زیر نوشتم، موقع نمونه سازی میایم و مستقیم فرام_برت رو صدا میزنیم و مقادیر رو میدیم بهش. بعد
در خود فرام_برت، میایم و 'سی ال اس'  که خود کلاس باشه رو بر می گردونیم که باعث فعال شدن اینیت می گردد. بعد
از فعال شدن اینیت می توانیم اینستنس وریبل ها که باید توسط اینستنس متود ها ساخته شود، را بسازیم

static methods:
متدهای 'استتیک' برخلاف متدهای 'کلاس' و 'اینستنس' هیچ مقداری را به عنوان اولین آرگومان نیاز ندارند
متدهای 'استتیک' متدهایی هستند که از نظر منطقی شبیه به کلاس مورد استفاده دارند اما نیازی به آبجکت یا خود کلاس ندارند
برای دسترسی بهش از خود کلاس یا آبجکت استفاده کنیم
نمونه کد:
Person.is_adult(18)
person_1.is_adult(18)



"""
import datetime



class Person:
    # class method
    @classmethod
    def from_birth(cls, name, height, age):
        reverse_age = datetime.datetime.now().year - age
        return cls(name, height, age=reverse_age)

    # instance | regular method
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    # instance | regular method
    def show_detail(self):
        print(f'{self.name} have {self.height}cm height and {self.age} years old.')

    # static method
    @staticmethod
    def is_adult(age):
        if 18 <= age <= 100:
            print('Yes')
        else:
            print('No')



person_1 = Person.from_birth('Mahdi', 170, 2003)
person_1.show_detail()
person_1.is_adult(18)