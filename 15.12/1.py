# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

n = input('Введите вещественное число:')
sum = 0 

for i in n:
    if i.isdigit():
        sum += int(i)
print(f'{n} -> {sum}')
