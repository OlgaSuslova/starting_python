def menu():
    op = int(input('1 - Добавить студента \n 2 - Добавить предмет \n 3 - Добавление оценки ученику по предмету \n 4 - Список учеников \n 5 - Лист оценок ученика \n 6 - Выход из программы \n'))
    return op


def input_student():    
    name = input('Введите фамилию и имя: ')
    return name


def input_less():
    less = input('Введите предмет: ')
    return less


def input_mark():
    name = input('Введите фамилию и имя: ')
    less = input('Введите предмет: ')
    mark = input('Введите оценку: ')
    return name, less, mark


def get_name_to_show():
    name = input('Введите фамилию и имя для просмотра оценок: ')
    return name