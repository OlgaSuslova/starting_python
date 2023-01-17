# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# from random import choice


# def make_equation(power):
#     if power <= 0:
#         return "Error! Enter a positive number."
    
#     equation = ""
#     nums_list = range(0, 10)

#     with open("equations.txt", "a", encoding="utf-8") as f:
#         while power > 0:
#             coef = choice(nums_list)
#             sign = choice(["+", "-"])
            
#             if coef:
#                 equation += f"{coef}*x^{power} {sign} "

#             power -= 1

#         f.write(f"{equation}{choice(nums_list)} = 0\n")

#     return "The equation is added in file equations.txt"

# k = int(input("Enter a power: "))
# print(make_equation(k))

import random 

k = int(input())
result = ""

for i in range(k, -1, -1):
    koeff = random.randint(0, 100)
    if koeff == 0:
        continue
    if koeff == 1:
        result += f"x**{i}** + "
        continue
    if i == 1:
        result += f"{koeff}*x + "
    elif i == 0:
        result += f"{koeff}"
    else:
        result += f"{koeff}*x**{i} + "

result += " = 0"
print(result)

f = open("filepol.txt", "w")
f.write(result)
f.close