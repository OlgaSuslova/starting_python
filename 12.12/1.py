# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

inputnumber = int(input('Введите цифру, обозначающую день недели: '))

if 0 < inputnumber < 6 :
    print(f'{inputnumber} -> нет')

elif inputnumber == 6 or inputnumber == 7:
    print(f'{inputnumber} -> да')
    
else:
    print(f'{inputnumber} -> Цифра не является днем недели')
    
