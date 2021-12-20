"""



__call__:
زمانی این متود فعال می شه که ما یک آبجکت از کلاس رو بصورت یک فانکشن صدا بزنیم
در دیزاین پترن سینگلتون کاربرد دارد



"""



class Person:
    
    def __call__(self, value, *args, **kwargs):
        print(value)



person_1 = Person()
person_1('Mahdi')