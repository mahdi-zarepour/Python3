"""



Collections.defaultdict:
بازگرداندن مقداری پیشفرض برای کلید های ناموجود
برای توضیحات به صفحات ۱۷۵ پایتون تریکس مراجعه کنید
بجای اینکه خطای کی ارور بخوریم یا از متود گت استفاده کنیم، باخیال راحت لیست رو بهش میدیم و 
با متود های لیست باهاش کار می کنیم. جالب بود که اگر از لیست استفاده نکنیم، بهمون ارور میده برای کلید ناموجود



"""
from collections import defaultdict

defaultdict_dict = defaultdict(list)
defaultdict_dict['book'].append('python tricks')
defaultdict_dict['book'].append('two scoops of django')
# print(type(defaultdict_dict))
# print(defaultdict_dict['book'])

error_dict = defaultdict()
error_dict['book'] = 'python tricks', 'two scoops of django'
print(type(error_dict))
print(error_dict['book'])
# print(error_dict['error']) # output => KeyError: 'error'
