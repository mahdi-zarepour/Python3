"""



Collections.OrderedDict:
دیکشنری به همراه کلید های دارای اولویت
برای توضیحات به صفحات ۱۷۴ تا ۱۷۵ مراجعه کنید
برای زمانی استفاده می شود که الگوریتم برنامه ما بر روی ترتیب ذخیره سازی در دیکشنری تمرکز دارد



"""

from collections import OrderedDict

ordered_dict = OrderedDict(
    one=1,
    two=2,
    three=3,
)
ordered_dict['four'] = 4
print(ordered_dict['one'])
print(ordered_dict.keys())
print(ordered_dict.values())
