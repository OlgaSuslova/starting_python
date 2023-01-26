import view, sort

def start():
    while True:
        op = view.menu()
        if op == 1:
            view.add_data()
        if op == 2:
            view.print_table()
        if op == 3:
            view.print_name()
        if op == 4:
            sort.sort_name()
        if op == 5:
            break