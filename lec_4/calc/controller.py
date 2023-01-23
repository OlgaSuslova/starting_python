import view 
import math_operator

def start():
    type = view.get_type()
    sign = 'error sign'
    if type:
        a, b = view.get_value_int()
    else:
        a, b = view.get_value_complex()

    math_operator.init(a, b)
    
    sign = view.get_sign(type)
    if sign == '+':
        res = math_operator.summ()
    elif sign == '-':
        res = math_operator.diff()
    elif sign == '*':
        res = math_operator.multy()
    elif sign == '/':
        res = math_operator.dell()
    elif sign == '//':
        res = math_operator.cel_del()
    elif sign == '%':
        res = math_operator.summ()

    view.out_res(res)


