"""

Mutable Default Argument

در پایتون، هنگام تعریف فانکشن، هیچوقت نباید از آبجکت های تغییرپذیر بعنوان دیفالت آرگیومنت درنظر گرفت
داستان از این قراره که، دیفالت آرگیومنت هایی که تغییرپذیرند مثل لیست، فقط و فقط یکبار ایجاد می شوند و
آن هم هنگام ایجاد خود فانکشن است! در نتیجه هربار که ما فانکشن رو صدا بزنیم، آبجکت میوتیبل از اول ساخته
نمی شود و بلکه دوباره از همان اولیه استفاده خواهد شد

راه حل چیه؟
بیایم دیفالت رو برابر نان قرار بدیم و چک کنیم اگر نان بود بیاد و یک لیست رو بسازه

"""

# Wrong Way
# def show(name, person=[]):
#     person.append(name)
#     return person


# s1 = show('Mahdi')
# print(s1) # output => ['Mahdi']
# s2 = show('Rose')
# print(s2) # output => ['Mahdi', 'Rose']
# s3 = show('Ali')
# print(s3) # output => ['Mahdi', 'Rose', 'Ali']

# -------


# Right Way
def show(name, person=None):
    if person is None:
        person = []
    person.append(name)
    return person


s1 = show('Mahdi')
print(s1) # output => ['Mahdi']
s2 = show('Rose')
print(s2) # output => ['Rose']
s3 = show('Ali')
print(s3) # output => ['Ali']