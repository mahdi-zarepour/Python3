"""


دکوریتور پراپرتی:
با این دکوریتور می توانیم کاری کنیم که متد ها، مانند پراپرتی ها قابل استفاده باشد
یعنی بدون نیاز به پرانتز بتونید متدهاتون رو صدا بزنید
ما می توانیم از دکوراتور پراپرتی برای مشخص کردن 'ستر' و 'دلیتر' نیز استفاده کنیم

Property:
اگر ما یک متود را بدون پرانتز صدا بزنیم، خود اون متود رو برای ما بر می گردونه و
اون متود رو اجرا نمی کنه
@property

Setter:
ما با تعریف دکوریور پراپرتی، تنها به متود دسترسی خواندن داشتیم اما اگر بخواهیم
مقدار جدیدی را ست کنیم، باید از ستر اسفاده کنیم
روش تعریف آن بصورت زیر است:
@name.setter   #property-name.setter decorator

Deleter:
هرگاه بخواهیم پراپرتی را حذف کنیم، این متود فعال می شود
del property => @name.deleter 



"""



class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
            return f'{self.first_name} {self.last_name}'
    
    @full_name.setter
    def full_name(self, first_name):
        if isinstance(first_name, str):
            self.first_name = first_name
        else:
            raise ValueError('first name most a string')

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None




person_1 = Person('Mahdi', 'Zarepour')
person_1.full_name # property
person_1.full_name = 'Ali' # setter
del person_1.full_name # deleter
