# Задача 32:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input('Введите число А: '))
b = int(input('Введите целое число В: '))

def rec(a, b):
    if b in [0, 1]:
        return 1
    else:
        return a**b

print(rec(a,b))

