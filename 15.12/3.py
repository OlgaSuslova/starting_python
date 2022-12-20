# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
    
#     *Пример:*
    
#     - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06


n = int(input('Введите число N:'))

list = {}
count = 0

for i in range(1, n + 1):
    list[i] = round((1 + 1/i) ** i, 2)
    count = count + round((1 + 1/i) ** i, 2)

print(list)
print(f'Сумма = {count}')

