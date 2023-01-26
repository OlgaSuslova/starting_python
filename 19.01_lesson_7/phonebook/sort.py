def sort_name():
    with open('worker_list.txt', 'r') as file:
        lst = file.readlines()
        lst_with_names = []
        for line in lst:
            a = line.strip().split(',')
            lst_with_names.append(a)
        lst_with_names = sorted(lst_with_names, key = lambda x: x[1])
        string_ = ''
        for worker in lst_with_names:
            res = ','.join(worker)
            string_ += res + '\n'
    with open('worker_list.txt', 'w') as file:
            file.write(string_)
