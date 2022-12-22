# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


list = [1.1, 1.2, 3.1, 5, 10.01]

newlist = []

for i in range(len(list)):
    if type(list[i]) == float:
        newlist.append(round(list[i] - int(list[i]), 2))

print(f'{list} => {max(newlist) - min(newlist)}')
