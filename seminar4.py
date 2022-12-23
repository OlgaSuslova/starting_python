# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# list_num = input().split()
# list_num =list(map(int,list_num))
# print(max(list_num),min(list_num))


# second decision
# a = input('Введите строку: ')
# b = a.split()
# print(b)
# for i in range(len(b)):
#     b[i] = int(b[i])
# print(b)
# print(max(b), min(b))




# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

# a = int(input())
# b = int(input())
# c = int(input())
# d = b**2 - 4*a*c

# if d<0:
#   print("корней нет")
# elif d == 0:
#   x = (-1)*b/2*a
#   print(x)
#
# else:
#   x1 = (-b + math.sqrt(d))/2*a,2
#   x2 = (-b - math.sqrt(d))/2*a
#   print(x1,x2)


# 29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# a = int(input())
# b = int(input())
# for i in range(2,min(a,b)):
#     if a%i == 0 and b%i == 0:
#         print(i)

# # teacher
# a = int(input())
# b = int(input())
# for i in range(max(a,b),a*b,max(a,b)):
#     print(i)
#     if i%a==0 and i%b==0:
#         print(i)
#         break


# from math import lcm
# a = 4
# b = 10
# print(lcm(a,b))