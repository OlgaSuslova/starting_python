# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# def prime_factors(number):
#     result = []
#     i = 2

#     while number > 1:
#         if number % i == 0:
#             result.append(i)
#             number //= i
#         else:
#             i += 1
    
#     return result


# num = int(input("Введите натуральное число N: "))
# print(prime_factors(num))


n = int(input("Введите натуральное число N: "))
list_num = []
current_num = 2
while n!=1:
    if n%current_num == 0:
        list_num.append(current_num)
        n = n // current_num
        current_num = 2
    current_num += 1
print(list_num)
