"""



نوع داده ای بولین دو مقدار دارد: تروو و فالس. اگر آبجکت داندر بوول را نداشته باشد، داندر لن را مبنا قرار می دهد و 
اگر داندر لن را هم نداشته باشد، تروو بر می گرداند. تمام دنباله ها اگر خالی باشند، فالس برگردانده می شود
در شروط هم اگر مستقیم خود آبجکت را مورد بررسی قرار دهیم، داندر بوول چک می شود


__bool__:
متد 'بوول' یک متد داخلی پایتون است که برای تست درستی آبجکت‌ها استفاده می شود
این متد یک آبجکت گرفته و مقدار 'تروو' یا 'فالس' را برمی گرداند
سینتکس کلی آن به شکل زیر است:
bool([x])

متد 'بوول' به شکل زیر کار میکند:
A:
اگر یک آبجکت، متد 'داندر بوول' را در خود داشته باشد، از مقدار برگشتی این متد استفاده می کند
اگر متد 'داندر بوول' نباشد، متد 'داندر لن' را بررسی میکند و از مقدار برگشتی این متد استفاده می کند
B:
اگر آبجکت به هر شکلی صفر باشد،‌ 'فالس' برمی گرداند
C:
اگر آبجکت خالی باشد، 'فالس' برمی گرداند، مثلا یک 'استرینگ' خالی یا یک تاپل خالی
D:
اگر آبجکت 'نان' باشد نیز 'فالس' برمی گرداند
E:
اگر هیچ یک از متدهای 'داندر بوول' و 'داندر لن' نباشند، به طور پیشفرض مقدار 'تروو' برگشت داده خواهد شد



"""



# a = 1
# b = 'amir'
# c = []

# print(bool(a))
# if b:
#     print('b is True')
# if c:
#     print('c is True')



class Person:

    def __init__(self, name=None, family=None, age=None):
        self.name = name
        self.age = age
        self.family = family

    def __bool__(self):
        return bool(self.name)

    def __len__(self):
        return len(self.family)



person_1 = Person('Mahdi', 'Zarepour', 18)


if person_1:
    print('True')
else:
    print('False')