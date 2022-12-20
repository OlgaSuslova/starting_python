# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число N:'))

list = []

for i in range(-n, n + 1):
    list.append(i)
print(f'Последовательность чисел от -N до N: {list}') 

file = open("file.txt", "r")
num = file.readlines()
for i in range(len(num)):
    num[i] = int(num[i].strip())
print(f'Позиции из файла: {num}')

product = 1
for i in range(len(num)):
    product *= list[num[i]]
print(f'Произведение элементов: {product}')



