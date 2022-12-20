# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27,

number = int(input('Введите число:'))
num = 1

for i in range(number):
    print(num, end = ' ')
    num = num * -3


n = int(input())
num = 1
print(num, end = " ")
for i in range(1,n):
    num*=-3
    print(num, end = " ")

for i in range(n):
    print((-3)**(i))


# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Введите число:'))


# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input())
a = {}
for i in range(1,n+1):
    a[i] = i*3+1
print(a)



# 13. Напишите программу, в которой пользователь будет задавать две строки, 
# # а программа - определять количество вхождений одной строки в другой.
str_1 = input('Введите 1-ую строку: ')
str_2 = input('Введите 2-ую строку: ')

print(str_1.count(str_2))


one = input()
two = input()
count = 0
for i in range(len(one)-len(two)+1):
    if one[i:i+len(two)] == two:
        count += 1
print(count)
print(one.count(two))


# 1)Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.


import random

n = int(input())
list = []

for i in range(n):
    list.append(random.randint(2, 5))

print(list)

max = 0
for i in range(n):
    if list.count(list[i]) > max:
        max = list.count(list[i])

print(max)


# решение учителя
###
import random

list_num = []
max = 0
for i in range(10):
    a= random.randint(2,5)
    list_num.append(a)
print(list_num)
print(set(list_num))
for i in set(list_num):
    if list_num.count(i)>max:
        max = list_num.count(i)
print(max)

###
import random

a = 1
b = 6

array = [random.randint(a, b) for i in range(20)]
print(array)

print(set(array))
d = {}

for i in array:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

max = 0
for i in range(a, (b + 1)):
    if (d[i] > max):
        max = d[i]

print(f"Максимальное повторение элемента {max} раз.")


#второе решение
import random

number = int(input())
maxRandom = int(input('input max random number'))
maxAmount = 0

list = []
count = [0] * (maxRandom+1)

for i in range(0, number):
    list.append(random.randint(0, maxRandom))

for i in list:
    count[int(i)] += 1

for i in count:
    if i > maxAmount:
        i = maxAmount

print(list)
print(count)
print('МАскимально количество раз появилась ' + str(count[maxAmount]) + ', ' + str(maxAmount+1) + ' раз')

#третьте решение
import random

number = int(input())
maxRandom = int(input('input max random number'))
maxAmount = 0

list = []
count = [0] * (maxRandom+1)

for i in range(0, number):
    list.append(random.randint(0, maxRandom))

for i in list:
    count[int(i)] += 1

for i in count:
    if i > maxAmount:
        i = maxAmount

print(list)
print(max(count))
print('МАскимально количество раз появилась ' + str(count[maxAmount]) + ', ' + str(maxAmount+1) + ' раз')

# 2)Данная программа должна вывести n рядов, заполненных знаком ‘*’ определенным образом. 
# А именно: в первом ряду должно быть n «звездочек», в втором n-1, и так далее. 
# А в последнем ряду таким образом будет одна «звездочка». 
# Причем убывать эти «звездочки» должны слева направо. Число n вводится пользователем.
# Введите количество рядов: 5
# *****
# ****
# ***
# **
# *

n = int(input())

for i in range(n, 0, -1):
    print('*' * i)
