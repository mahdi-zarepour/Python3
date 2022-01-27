"""

Compration Methods: __lt__, __le__, __eq__, __ne__, __gt__, __ge__

__lt__ => lower than x < y

__le__ => lower equal x <= y

__eq__ => equal x == y

__ne__ => not equal x != y  or  x <> y

__gt__ => greater than x > y

__ge__ => greater equal x >= y



بصورت پیشفرض پایتون کاری به متود های مقایسه ای نداره و از دیفالت خودش استفاده می کنه
ما می توانیم رفتار پیشفرض را تغییر بدهیم با متود های مقایسه ای
نکته: زمانی که ایکوال رو ساختیم، نات ایکوال هم بسازیم
متود های مقایسه ای در آخر نوع داده ای بولیین بر میگردونند

این متودها دوتا ورودی می گیرند، سلف و آدر. مقدار سمت چپ میشه سلف و مقدار سمت راست میشه آدر

نکته: ما باید چک کنیم که آیا اصلا دوتا آبجکتی که دارند با یکدیگر مقایسه می شوند، از یک کلاس هستند یا نه
"""


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and self.age == other.age
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.name != other.name or self.age != other.age
        return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.age < other.age
        return False

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.age <= other.age
        return False

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.age > other.age
        return False

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.age >= other.age
        return False


class Alien:
    def __init__(self, name, age):
        self.name = name
        self.age = age


h1 = Human('Mahdi', 18)
h2 = Human('Mahdi', 18)
h3 = Alien('Mahdi', 18)


print(h1 == h3) # is instance ???


print(h1 == h2) # __eq__

print(h1 != h2) # __ne__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__