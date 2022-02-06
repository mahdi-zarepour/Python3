"""



comprehension == درک مطلب

List Comprehension:
لیست کامپرهنشن پایتون راهی برای ایجاد یک لیست بر اساس لیستی دیگر است. درواقع راهی ساده تر برای ایجاد لیست
لیست کامپرهنشن معمولاً برای فیلتر کردن موارد از لیست یا تغییر مقادیر موجود در لیست استفاده می شود
لیست کامپرهنشن در داخل پرانتز قرار می گیرد. هنگامی که با لیست ها کار می کنید، ممکن
است بخواهید یک لیست بر اساس محتویات یک دنباله موجود ایجاد کنید
به عنوان مثال، ممکن است بخواهید یک لیست بر اساس دنباله ای از کاراکترها ایجاد کنید
یا ممکن است بخواهید لیستی را ایجاد کنید که محتویات یک لیست دیگر را در دو ضرب کند
اینجاست که لیست کامپرهنشن وارد کار می شود

ساختار نگارش کلی لیست کامپرهنشن در پایتون به شکل زیر هست:
[output expression forloop if sentence]



"""


# define a list to contain number from one to ten but them should even

# 1
nums = [2, 4, 6, 8, 10]


# 2
x = []
for num in range(1, 11):
    if num % 2 == 0:
        x.append(num)


# 3
list_comprehansion = [num for num in range(1, 11) if (num%4==0)]
# -------------


# Hard Example
# list = [(1, 'odd'), (2, 'even'), (3, 'odd')]


x = []

for num in range(1, 11):
    if num % 2 == 0:
        x.append((num, 'even'))
    else:
        x.append((num, 'odd'))


list_comprehansion = [(num, 'Even' if (num%2==0) else 'Odd') for num in range(1, 11)]
