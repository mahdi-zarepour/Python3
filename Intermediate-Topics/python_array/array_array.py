"""



array.array:
ساختمان داده آرایه همان ساختمان داده آرایه تغییرپذیر است با این تفاوت که فقط یک نوع داده در خود ذخیره می کند
برای مطالعه بیش تر به کتاب ترفند های پایتون صفحه ۱۸۱ مراجعه کنید



"""
# (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
from array import array

array_1 = array('u', ['a', 'b', 'c',])
array_2 = array('f', [1.0, 2.0, 3.0,])

print(array_1)
print(array_1[1])

array_2.append(4.0)
print(array_2)
print(array_2[1])
