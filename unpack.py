def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params() # Вызов без аргументов
print_params(25, 'Салам Алейкум', False) # Вызов со всеми аргументами
print_params(1, [5, 5]) # Вызов с двумя аргументами и изминением одного

values_list = [1 , True, [3, 2, 1]]
values_dict = {'a': 'Hello', 'b': 5.244, 'c': [123, 321]}

print_params(*values_list) # Вызов распакованного списка
print_params(**values_dict) # Вызов распакованного словаря

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)