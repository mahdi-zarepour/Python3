"""



logging:
ماژول "لاگین" در پایتون ابزاری قدرتمند برای ایجاد کردن "لاگ" برای برنامه است
لاگ ها به شما اجازه میدن عملکرد برنامه تون رو تحت کنترل داشته باشید و
اگه برنامه تون به مشکل خورد، خیلی سریع متوجه بشید
پیغام هایی که داخل لاگ ها ذخیره میکنید به شش دسته تقسیم می شوند:
((NOSET = 0), (DEBUG = 10), (INFO = 20), (WARNING = 30), (ERROR = 40), (CRITICAL = 50))
فقط سه تا از پنج تا دسترسی به ما پیغامی نشون می دهند. وارنینگ، ارور، کریتیکال

basicConfig()
در این ماژول یک متودی وجود دارد که پارامتره های مختلفی می گیرید



"""
import logging


logging.basicConfig(
    filename='/home/mahdi/Desktop/Project/'
    'Python/Python/Intermediate-Topics/logging_module/msg.log',
    level=logging.ERROR,
    format='%(levelname)s-%(asctime)s-%(filename)s-%(message)s',
)

name = {
    'name': 'mahdi',
}

try:
    print(name['age'])
except Exception:
    # logging.error('gives an error', exc_info=True)
    logging.exception('gives an error')
