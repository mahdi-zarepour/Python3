"""



types MappingProxyType:
ساخت دیکشنری های فقط خواندنی
برای مطالعه بیشتر به صفحه ۱۷۶ کتاب ترفندهای پایتون مراجعه کنید
یکی از بهترین ساختمان داده های دیکشنری! ساخت دیکشنری های غیر قابل تغییر



"""

from types import MappingProxyType

writable_dict = {
    'one': 1,
    'two': 2,
    }

readable_dict = MappingProxyType(writable_dict)

print(readable_dict['one'])
# print(readable_dict['three']) # output => KeyError: 'three'

writable_dict['three'] = 3
print(readable_dict['three'])
