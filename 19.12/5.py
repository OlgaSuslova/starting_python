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



# решение учителя
# def postive_fib(n):
#   postive_list = [0,1]
#   for i in range(n-1):
#       postive_list.append(postive_list[-2]+postive_list[-1])
#   return postive_list
#
# def negative_fiv(n):
#   negative_list = [0,1]
#   for i in range(n-1):
#       negative_list.append(negative_list[-2]-negative_list[-1])
#   return negative_list
#
#
# print(negative_fiv(8)[::-1] + postive_fib(8)[1:])