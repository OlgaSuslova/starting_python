# Задача 31: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]


li = [int(i) for i in input('Введите элементы массива через пробел: ').split()]
print(list)

min = int(input('Введите минимальное число: '))
max = int(input('Введите максимальное число: '))

new = [i for i in range(len(li)) if min<li[i]<max ]
print(new)




# вывод элементов:
# new = list(filter(lambda x: min<x<max, li))
# print(new)