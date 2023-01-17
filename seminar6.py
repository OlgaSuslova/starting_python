#lambda, filter, map, zip, enumerate, list comprehension

#list comprehension
# import random

# a = [i for i in range(1,10) if i%2==0]
# print(a)

#enumerate

# a = [2, 4, 6, 8]
# for indx,val in enumerate(a):
# if val>5:
# a[indx] = 0
# print(a)

#zip
# a = [1,2,3]
# months = ["june","july","july1","july2","july3","july4"]
# dit_s = {1:"ddd",2:"112"}
# result = list(zip(a,months,dit_s))
# print(result[1][1])

#lambda
# def summ(a,b,*args):
# for i in args:
# print(i)
# return a+b
# print(summ(2,3,4,5,6,7))

# summ = lambda a,b: a+b if a>5 else 0
#
# for i in range(10):
# print(summ(7,3))

#map
# a = [(2,4,3),(4,5,6),(1,2,3)]
#
# a = list(map(lambda x:x[0]*x[1]*x[2],a))
# print(a)

#filter
# a = [2,4,3,4,5,6,1,2,3]
#
# res = list(filter(lambda x: True if x%2==0 else False,a))
# print(res)

#sorted
# a = [(6,5,5),(4,5,5),(1,2,3)]
# res = sorted(a,key = lambda x: (x[2],x[1],x[0]),reverse=True)
# print(res)







# ЗАДАЧИ

# 41)Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda, filter.
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]

arr1 = [1, 2, 3, 5, 7, 8, 9, 10]
arr2 = [1, 2, 4, 8, 9]

result = list(filter(lambda x: x in arr1, arr2))
print(result)




# 42)Имеется упорядоченный список:

# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Перебрать все элементы этого списка с помощью функций enumerate и элементы, 
# стоящие на главной диагонали (имеющие равные индексы со списком и индексом элемента внутри списка), 
# превратить в нули.

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


for index, value in enumerate(A):
   value[index] = 0
print(A)




# 43)Имеется список id сотрудников из 10 элементов, 
# каждый id - случайное число от 1 до 100 (сделать с помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов (вручную)

# Сопоставьте каждому имени сотрудника его id по порядку, и выведите получившийся список кортежей.
# Отсортировать список по возрастанию id.

# Выведете имена сотрудников, получившие нечетное id.

# Решить с помощью zip,filter,lambda

import random
ids = random.sample(range(1, 100), 10)
names = ['olga', 'alex', 'masha', 'tanya', 'oleg', 'nata', 'polina', 'marya', 'alexandr', 'elena']

res = list(zip(ids, names))
print(res)
print()

res = sorted(res)
print(res)
print()

odd_list = list(filter(lambda x: x[0]%2==1, res))
print(odd_list)

names_list = list(map(lambda x: x[1], odd_list))
print(names_list)