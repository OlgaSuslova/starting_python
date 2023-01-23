def get_type():
    type = int(input("Введите тип. 0 - комплексные, 1 - целые: "))
    return type


def get_value_int():
    a = int(input("a = "))
    b = int(input("b = "))
    return a, b


def get_value_complex():
    a = complex(input("a = "))
    b = complex(input("b = "))
    return a, b


def get_sign(type):
    if type:
        sign = input('sign:  ')
        if sign in ['+', '-', '*', '/', '%', '//']:
            return sign
        else:
            print('error input')
    else:
        sign = input()
        if sign in ['+', '-', '*', '/']:
            return sign
        else:
            print('error input')



def out_res(res):
    print(res)