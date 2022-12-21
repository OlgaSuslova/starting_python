# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]

list_product = []

if len(list)%2 == 0:
    for i in range(int(len(list)/2)):
        list_product.append(list[i] * list[len(list) - i - 1])

else:
    for i in range(int(len(list)/2 + 1)):
        list_product.append(list[i] * list[len(list) - i - 1])

    
print(f'{list} => {list_product}')