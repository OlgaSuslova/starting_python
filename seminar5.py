# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# print('Введите последовательность натуральных чисел через пробел')
# data = list(map(int,input().split()))
# for i in range(len(data)-1,-1,-1):
#     if i > 0:
#         number = data[i]
#         n = data[i-1]
#         if number - 1 != n:
#             x = number-1
#             data.append(x)

# print(f'Нужное нам чило = {x}')


# list1 = [1, 3, 4, 5, 6, 7]

# def find(list):
#     for i in list:
#         if list[i] -1 != list[i-1]:
#             return list[i] -1
# print(find(list1))

# 36. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.

# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# data = [1, 5, 2, 3, 4, 6, 1, 7]
# list = []
# m = 0
# for i in range(len(data)):
#     if data[i] > m:
#         list.append(data[i])
#         m = data[i]
# print(list)

# def posled(data):
#     result = []
#     flag = False
#     length=len(data)
#     for i in range(length-1):
#         for j in range(i+1,length):
#             if data[j]>data[i]:
#                 flag = True
#                 begin = i
#                 next = j
#                 break
#         if flag:
#             break
#     if flag:
#         result.append(data[begin])
#         result.append(data[next])
#         for i in range(next+1,length):
#             if data[i]>result[-1]:
#                 result.append(data[i])
#         return result
#     else:
#         return -1

# data = [7, 5, 2, 3, 4, 6, 1, 7]
# data_posled = posled(data)
# print(data_posled)

# 37. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# первое решение
# line = 'фывабвйцу кенабвджэ, ячсабвнгш, йцукенгвба'
# while ',' in line or '.' in line or ';' in line or ',' in line:
#     line = line.replace(',', '')
# print(line)

# arr = line.split()
# print(arr)

# arr2 = []
# for word in arr:
#     if 'абв' not in word:
#         arr2.append(word)
# print(arr2)

# второе решение
# data = 'аф фыв ыва ываабв, ывадлойц. Оывало абвываф, длоываабв.'

# data = ' '.join(list(filter(lambda slovo: not 'абв' in slovo, data.split())))
# print(data)


# text = "Привет, меабв! аааа вабв вабвб аааб, пабв абв"

# text = text.split()

# text_new = []
# for i in range(len(text)):
#     if "абв"  not in text[i]:
#         text_new.append(text[i])
# print(" ".join(text_new))