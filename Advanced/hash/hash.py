"""



Hash Method:
در پایتون این متد مقدار هش یک آبجکت رو نشون میده
مقدار هش همیشه نوع عددی هستش و مقدارهای هش هیچگاه در طول برنامه تغییر نمی کنند
به همین خاطر آبجکت های هشیبل رو میشه به عنوان کلید در دیکشنری پایتون استفاده کرد
پایتون از مقدار هش برای سرعت دهی به خواندن اطلاعات استفاده میکند
تقریبا تمام آبجکت های تغییرناپذیر هشیبل و آبجکت های تغییرپذیر هشیبل نیستند

آبجکت های هشیبل چیست:
آبجکت هایی هستند که هش ولیو آن ها هیچوقت در طول زندگیشان تغییر نمی کند
هشیبلیتی اجازه می دهد تا یک آبجکت به عنوان کلید های دیکشنری یا 'ست ممبر' ایجاد کنیم، بخاطر اینکه این دیتااستراکچرها
بصورت داخلی از آبجکت های هش ولیو استفاده می کنند


A:
از پایتون 3.3 به بعد برای مسائل امنیتی، هربار که کد رو ران کنیم، مقدار هش نیز تغییر میکند
پایتون برای خواندن و مقایسه کردن مقادیر از این اعداد که هش باشند، استفاده می کنه
مثلا با استفاده از عملگر ==  و 'ایس' پایتون به بررسی مقدار هش شده بین دو چیزی که داره مقایسه می شود، مبادرت می کند


B:
سرعت خواندن اطلاعات در دیکشنری و تاپل خیلی خیلی بیشتر از لیست ها است. علت:
آبجکت های تغییر پذیر(میوتیبل) هیچکدام هشیبل نیستند و آبجکت های تغییرناپذیر(ایم میوتیبل) تماما هشیبل هستند
برای مقایسه اطلاعاتی که در پایتون ذخیره می کنیم، پایتون نیازمند یک عدد ثابت در کل برنامه است و با اون عدد
عملیات مقایسه رو انجام بده. از اونجایی که اگر ما لیست رو تغییر بدیم، مقدار هش نیز تغییر می کند و دیگه 
پایتون نمی تونه تشخیص بده آیا این همون هش است یا نه؟ آیا همون لیسته یا لیست جدیده ساخته؟ اما داخل تاپل
و دیکشنری(کلیدها)، پایتون اینو هش می کنه و دیگه نمیتونیم تغییر بدیم
در دیکشنری ها، پایتون کلید رو از اعداد هش ست می کنه و دیگه نمی شه تغییرشون داد. در نتیجه برای کلیدها
نمی توان از مقادیر تغییر پذیر(میوتیبل) استفاده کرد. در زمان خواندن اطلاعات، پایتون از اعداد هش کلید ها
برای خواندن ولیو ها استفاده می کنه. پس اگر بخواد یک چیز قابل تغییر باشه، اگر اون تغییر پذیر، تغییر کند، پایتون
نمی تواند تشخیص دهد که یک چیز جدید ساخته شده یا همون قبلی است


C:
زمانی که ما متود هش رو صدا می زنیم، داندر متود هش فعال می شود. این داندر هش، یکسری قواعد دارد:
1:
زمانی که ما یک کلاس ایجاد می کنیم و اگر بخواهیم داندر هش رو ایجاد کنیم، حتما باید داندر ایکوال رو ایجاد کنیم
2:
اگر ما داندر ایکوال رو در کلاس ایجاد کنیم و داندر هش رو ایجاد نکنیم، آبجکتی که از اون کلاس ساخته
می شود، دیگر هشیبل نیست و از آن نمی توان به عنوان کلید استفاده کرد
3:
اگر کلاس ما قراره آبجکت های میوتیبل ایجاد کند و متود ایکوال رو هم ایجاد کردیم، به هیچ عنوان داندر هش رو
ایجاد نکنیم چون هشیبل ها نیاز دارند تا هیچوقت تغییر نکنند

دیکشنری ها در پایتون چگونه ساخته می شوند:
از هش ها استفاده می شود و در پرفرمنس بهتر است و سرعت رو افزایش می دهد

__eq__:
اجازه می دهد دو آبجکت با هم مقایسه شوند
مقدار سمت چپ به عنوان سلف و مقدار سمت راست به عنوان آدر قرار می گیرد

با استفاده از داندر هش و ایکوال در کنار هم، پایتون از هش برای مقایسه استفاده می کند و
می توان به عنوان کلید دیکشنری نیز استفاده کرد


D:
برای بررسی هشیبل بودن از کتابخانه کالکشن استفاده می کنیم



"""

# A:
# a = 'Mahdi'
# b = 'Mahdi'

# print(hash(a)) # -4525523434267650737
# print(hash(b)) # -4525523434267650737

# print(a == b) # True
# print(a is b) # True



# B:
# a = ['Mahdi', 'Ali']
# print(hash(a)) # TypeError: unhashable type: 'list'  =>  Because list is not hashable and mutable


# b = ('Mahdi', 'Ali')
# print(hash(b)) # -2366385910865737334  =>  Because Tuple is Hashable and Immutable



# c = {a: 'test'} # TypeError: unhashable type: 'list'



# C:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __hash__(self):
#         return hash(self.name)

#     def __eq__(self, other):
#         if self.age == other.age:
#             return True
#         return False



# p1 = Person('Mahdi', 18)
# p2 = Person('Mahdi', 20)

# print(p1 == p2) # __eq__

# without __hash__, hash value is different
# print(hash(p1)) # -5224277983420489087 => Because __hash__
# print(hash(p2)) # -5224277983420489087 => Because __hash__


# a = {p1: 'test_1', p2: 'test _2'}
# print(a[p1]) # output => test_1



# D:
from collections.abc import Hashable


list = ['list'] # False
tuple = ('tuple',) # True
dict = {2: 1} # False
set = {1, 2} # False
string = 'string' # True
integer = 1 # True
float = 1.0 # True


print(isinstance(list, Hashable))
print(isinstance(tuple, Hashable))
print(isinstance(dict, Hashable))
print(isinstance(set, Hashable))
print(isinstance(string, Hashable))
print(isinstance(integer, Hashable))
print(isinstance(float, Hashable))