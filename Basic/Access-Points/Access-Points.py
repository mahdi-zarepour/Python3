"""



Access Points => Public, Protected, Private


در هر زبان برنامه نویسی شی گرایی این مبحث وجود دارد و فقط سینتکس شان با هم فرق دارد
برای اینکه بتونیم دسترسی کلاس های فرزند رو به متدها و ویژگی های کلاس پدر محدود
کنیم(کجاها در دسترس باشه و کجا نباشه)، میتونیم از اکسس پوینت استفاده کنیم
این محدود کننده ها در پایتون به شکل _ و __ هستند
تمام قوانینی که برای کلاس وریبل ها وجود دارد، برای کلاس متود ها نیز صادق است

Public:
    نمی خواهد هیچ آندرلاینی قرار دهیم
    عمومی است و همه جا قابل دسترس

Protected:
    از یک آندرلاین قبل از اسم آن استفاده می کنیم
    مانند پابلیک در همه جا قابل دسترس است ولی این آندرلاین برای اینه که به برنامه نویس بفهمونه این متود مهم است
    پایتون زور نمی کنه! اما بطور قراردادی فقط در خود کلاس یا کلاسی که ارث بری کرده استفاده شود

Privete:
    از دو آندرلاین قبل از اسم آن استفاده می شود
    فقط در خود کلاس قابل دسترس است. نه در داخل کلاس ارث بری شده و نه جای دیگری
    همچنان پایتون زور نمی کنه!
    ما می توانیم با استفاده از نیم منگلینگ بهش دسترسی داشته باشیم
    Class._class-name__variable



"""



class Mammal:

    # Public
    leg = 4

    # Protected
    _maximumـlife = 1000

    # Private
    __sel = 'Eukaryotes'


    # Private Method
    def __private(self):
       return 'this is Private Method'



class Human(Mammal):
    
    def show(self):
        return self._maximumـlife



# Access Points of Public:
print(f'Public: {Mammal.leg}')
print(f'Public: {Human.leg}')



# Access Points of Protected:
print(f'Protected: {Mammal._maximumـlife}')
person_1 = Human()
print(f'Protected: {person_1.show()}')



# Access Points of Private:
print(f'Private: {Mammal._Mammal__sel}') # name mangling

mammal_1 = Mammal()
print(f'Private: {mammal_1._Mammal__sel}')
print(f'Private Method: {mammal_1._Mammal__private()}')