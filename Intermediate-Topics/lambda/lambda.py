"""



lambda(arguments): manipulate(arguments)

Lambda:
توابع ناشناس معروف به لامبدا 
یک تابع ناشناس ممکن است تابعی باشد که بدون شهرت تعریف شده باشد
هنگام تعریف توابع عادی، ما از کلمه کلیدی "دف" در پایتون استفاده می کنیم، اما
هنگام تعریف توابع ناشناس از کلمه کلیدی "لامبدا" استفاده می کنیم
لامبدا روشی سریع برای ایجاد تابع است. عبارات لامبدا باید به ساده ترین شکل ممکن و به دور از هرگونه پیچیدگی نوشته شوند
ابتدا با استفاده از کلمه کلیدی "لامبدا" مشخص میکنید که قراره یک لامبدا داشته باشید
بعد از اون پارامتر هایی که قرار است عبارت لامبدا داشته باشه رو مینویسید
و در آخر کاری قراره روی آرگومان ها انجام بشه رو مینویسید
دقت کنید که عبارت لامبدا هر تعدادی که بخواهید می تواند آرگومان
داشته باشد اما فقط یک (دستکاری-اعمال نفوذ) خواهد داشت و همچنین خودشان مقدار پردازش شده را ریترن می کنند


چرا از عبارت لامبدا استفاده کنیم:
پایتون با لامبدا به شکل یکسان با فانکشن‌های معمولی برخورد می کند
به نوعی، لامبدا شکلی جمع و جور برای نوشتن توابع ارائه می دهد که یک عبارت را باز می گرداند
با این حال، شما باید بدانید که استفاده از لامبدا چه زمانی مناسب است و چه زمانی از آنها اجتناب کنید
یکی از مهمترین موارد استفاده رایج برای لامبدا برنامه نویسی فانکشنال
است زیرا پایتون از پارادایم (یا سبک) برنامه نویسی که به عنوان برنامه نویسی فانکشنال شناخته می شود پشتیبانی می کند
لامبدا به شما این امکان را می دهد که یک تابع را به عنوان پارامتر
به یک تابع دیگر (به عنوان مثال، در "مپ" "فیلتر" و غیره) ارائه دهید
در چنین مواردی، استفاده از "لامبدا" به لطف ایجاد یک تابع یک بارمصرف، مفید است
در محیط پروداکشن هرگز نباید توابع لامبدا پیچیده را بنویسید، زیرا
رمزگشایی برای کد نویسان که کد شما را حفظ می کنند بسیار دشوار است
اگر خودتان را در حال ساختن عبارات پیچیده تک خطی کشف کردید، بهتر است با "دف" یک فانکشن کامل بنویسید


filter:
تابع "فیلتر" برای فیلتر کردن برخی عناصر خاص از یک دنباله استفاده می شود
دنباله مورد استفاده در این تابع یک آبجکت ایتریبل مانند لیست ها، مجموعه ها، چندتایی ها و غیره است
برای دریافت اطلاعات پردازش شده از طریق فیلتر، یا باید تبدیل به لیست کرد یا حلقه زد


map:
تابع "مپ" برای استفاده از یک عملیات خاص برای هر عنصر در یک دنباله استفاده می شود
برای دریافت اطلاعات پردازش شده از طریق مپ، یا باید تبدیل به لیست کرد یا حلقه زد



"""

# --- map()

# map_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def multi(number):
#     return number * number

# multi_lambda = map(lambda num: num * num, map_list)

# # print(list(map(multi, map_list)))
# print(list(multi_lambda))


# --- filter()

# filter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def even(num):
#     if num % 2 == 0:
#         return True
#     return False

# even_lambde = filter(lambda num: num % 2 == 0, filter_list)

# print(list(even_lambde))
# print(list(filter(even, filter_list)))


# --- sorted()

x = [(5, 'b'), (4, 'v'), (3, 'a'), (1, 'e')]

# print(sorted(x)) # sort by numbers: [(1, 'e'), (3, 'a'), (4, 'v'), (5, 'b')]

print(sorted(x, key=lambda i: i[1])) # sort by char: [(3, 'a'), (5, 'b'), (1, 'e'), (4, 'v')]
