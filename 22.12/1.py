# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = input('Введите степень округления в формате 0.01 от 10 в степени -1 до 10 в степени -10 -> ')
d = d[2:len(d)]
print(round(math.pi,len(d)))



#Вычислить число c заданной точностью d
#при $d = 0.001, π = 3.141.$
# import math
# n = input()
# length = len(n.split(".")[1])
# print(round(math.pi,length))
