# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


k = int(input('Введите число:'))


positive_list = [0, 1]

for i in range(k-1):
    positive_list.append(positive_list[-2] + positive_list[-1])


negative_list = [0, 1]

for i in range(k-1):
    negative_list.append(negative_list[-2] - negative_list[-1])


print(f'k = {k} => {negative_list[::-1] + positive_list[1::]}')
