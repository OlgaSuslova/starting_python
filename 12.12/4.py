# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

inputnumber = int(input('Введите номер четверти: '))

if inputnumber == 1:
    print('Координаты первой четверти находятся в диапазоне точек Х(0, +∞] и У(0, +∞]')
elif inputnumber == 2:
    print('Координаты второй четверти находятся в диапазоне точек Х[-∞, 0) и У(0, +∞]')
elif inputnumber == 3:
    print('Координаты третьей четверти находятся в диапазоне точек Х[-∞, 0) и У[-∞, 0)')
elif inputnumber == 4:
    print('Координаты четвертой четверти находятся в диапазоне точек Х(0, +∞] и У[-∞, 0)')
else:
    print('Ошибка ввода!')