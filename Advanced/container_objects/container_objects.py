"""



container objects:
به آبجکت هایی گفته میشن که بتونید داخلشون با استفاده از کلمه کلیدی 'این' بگردید و چک کنید
که آیا یک مقدار خاصی در اون آبجکت وجود داره یا نه
برای کانتینر کردن آبجکت هاتون میتونید از متد روبرو استفاده کنید: __contains__
این متود ها معمولا داده بولیین بر می گردونند
در این متود، آیتم همون کلمه ای است که سمت چپ کلمه کلیدی 'این' قرار گرفته است



"""

class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __contains__(self, item):
        if item in self.country:
            return True


p1 = Person('Mahdi', 'Iran')

print('Iran' in p1)
print('USA' not in p1)
