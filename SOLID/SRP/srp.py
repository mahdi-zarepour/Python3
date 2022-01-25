"""

Single Responsibility Principle
هر کلاس و تابع، فقط و فقط مسئول انجام یک کار می باشد

"""

# non-SRP
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         return f'{self.name}'

#     # this method break SRP
#     def db_save(self):
#         print(f'{self.name} save.')


# p1 = Person('Mahdi', 18)
# p1.db_save()


# -------------



# SRP
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f'{self.name}'


class DB:
    def db_save(self):
        print('save')


p1 = Person('Mahdi', 18)
