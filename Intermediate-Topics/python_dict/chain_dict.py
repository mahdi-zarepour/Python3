"""



collections chainmap:
جستجوی چندین دیکشنری در یک مپینگ
برای توضیحات بیشتر به صفحه۱۷۶ از ترفند های پایتون مراجعه کنید
این یکی خیلی جالبه! چنیدن دیکشنری رو با هم یکی میکنه و از چپ به راست داخلش می گرده
اگر چیزی پیدا کرد بر میگردونه وگرنه ارور میده



"""

from collections import ChainMap

dict1 = {
    'one': 1,
    'two': 2,
    }
dict2 = {
    'three': 3,
    'four': 4,
    }

chain_dict = ChainMap(dict1, dict2)
print(chain_dict)
print(chain_dict['four'])
print(chain_dict['five'])
