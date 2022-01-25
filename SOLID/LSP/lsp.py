# LSP
# آبجکت های متفاوتی که از کلاس پدر ارث بری می کنند نباید با تغییر اون ها، کار بهم بریزه
# کلاس هامون رو بر اساس ویژگی پراپرتی ها نسازیم چرا که کلاس قراره حالت کلی رو مشخص کنه


# non lsp
# class Bird:
#     def __init__(self, name):
#         self.name = name

#     def fly(self):
#         print(f'{self.name} is flying')

# eagle = Bird('eagle')
# eagle.fly()

# penguin = Bird('penguin')
# penguin.fly() # output => penguin is flying !!! it٬s False



# lsp
class Bird:
    def __init__(self, name):
        self.name = name

class BirdFly(Bird):
    def fly(self):
        print(f'{self.name} is flying')

eagle = BirdFly('eagle')
eagle.fly()

penguin = Bird('penguin')
penguin.fly() # output => Error. penguin can٬t flying. it٬s True