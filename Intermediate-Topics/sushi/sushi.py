"""



sushi in python:
برای مطالعه بیش تر به کتاب ترفند پایتون صفحه ۲۲۴ مراجعه شود



"""

lst = [num for num in range(1, 11)]

reverse_lst = lst[::-1]
del lst[:]
print(lst)

second_lst = lst
lst[:] = [1, 2, 3,]
print(f'second_lst => {second_lst}')
print(lst is second_lst)

copied_lst = lst[:]
print(f'copied_lst => {copied_lst}')
print(lst is copied_lst)
