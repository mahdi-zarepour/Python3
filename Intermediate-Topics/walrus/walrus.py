"""

Walrus:
بزرگ ترین تغییر پایتون 3.8 عبارت تخصیصی با ساختار جدید است
ساختار این عبارت بصورت ":=" است. این عبارت به نام والروس شناخته می شود. از نظر لغوی به معنی شیر دریای است

عبارت والروس به شما امکان می دهد که یک مقدار را در یک عبارت اختصاص دهید و برگردانید
این عملگر درواقع دوتا کار رو همزمان انجام می دهد، اختصاص دادن(مقداردهی کردن) و برگرداندن: assign and return
مثال:
print( name := 'Mahdi ) => 
با این کار ما دستور دادیم مقدار نام رو برابر مهدی قرار بده و اون رو ریترن هم بکن. درواقع پرینت متغییر
نام رو چاپ نمی کنه، بلکه مقدار ریترن شده ی مهدی رو چاپ کرد


والروس در حلقه ها:
در حلقه، قبل از اینکه حلقه شروع بشه، من اینپوت رو از کاربر می گیرم و میریزم داخل کارنت و همزمان ریترن
می کنم به یک شرط و میگیم اگر برابر بود با شرط، بریک کن

"""

# First Method
# current = input('give me a number: ')
# inputs = list()

# while current != 'q':
#     inputs.append(current)
#     current = input('give me a number: ')

# print(inputs)



# Secend Method
# current = input('give me a number: ')
# inputs = list()

# while True:
#     current = input('give me a number: ')
#     if current == 'q':
#         break

#     inputs.append(current)

# print(inputs)



# Walrus Operator
inputs = list()

while (current := input('give me a number: ') != 'q'):
    inputs.append(current)
    print(current)


print(inputs)