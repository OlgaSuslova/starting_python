def menu():
    op = int(input('1 - добавить пользователя,\n 2 - вывести таблицу,\n 3 - вывести только имя и фамилию,\n 4 - отсортировать по имени,\n 5 - выход \n'))
    return op


def add_data():
    id = input('ID: ')
    firstname = input('Имя: ')
    lastname = input('Фамилия: ')
    number = input('№ телефона: ')
    comments = input('Комментарий: ')
    line = f'{id},{firstname},{lastname},{number},{comments}\n'
    with open('worker_list.txt', 'a') as file:
        file.write(line)
    print('Данные сохранены!\n')


def print_table():
    with open('worker_list.txt', 'r') as file:
        for line in file.readlines():
            print(line, end=' ')


def print_name():
    with open('worker_list.txt', 'r') as file:
        lst = file.readlines()
        for line in lst:
            a = line.split(',')
            print(f'Имя - {a[1]}, Фамилия - {a[2]}')