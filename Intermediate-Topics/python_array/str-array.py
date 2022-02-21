"""



str:
ساختمان داده "اس تی آر" برای ذخیره سازی دنباله ای از کاراکترهای یونیکد تغییرناپذیر است
برای حذف یا اضافه کردن عناصر، باید یک کپی از آن گرفت! اما نزدیک ترین عنوان برای "رشته تغییرپذیر"، ذخیره
هر کاراکتر از یک رشته به عنوان عناصر یک لیست است
برای مطالعه بیش تر به کتاب ترفند های پایتون صفحه ۱۸۲ مراجعه کنید



"""
immutable_arr = 'immutable'
# arr[0] = '' # output => TypeError: 'str' object does not support item assignment

mutable_arr = list('immutable')
del mutable_arr[0:2]
# print(mutable_arr) # output => ['m', 'u', 't', 'a', 'b', 'l', 'e']

mutable_arr_to_str = ''.join(mutable_arr)
# print(mutable_arr_to_str) # output => mutable
