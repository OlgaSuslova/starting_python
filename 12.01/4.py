# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
    # Для чисел:
    # Входные данные:
    # 111112222334445
    # Выходные данные:
    # 5142233415
    # Также должно работать и для букв:
    # Входные данные:
    # AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
    # Выходные данные:
    # 6A1F2D7C1A17E
    # (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
    # Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.


text = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
text2 = ''
text3 = ''
count = 1

for i in range(0, len(text)-1):
    if text[i] == text[i+1]:
        count +=1
        text2 = str(count) + text[i] 
    else: 
        text2 = str(count) + text[i] 
        count = 1
        text3 += text2
text3 += text2

print(text3)

