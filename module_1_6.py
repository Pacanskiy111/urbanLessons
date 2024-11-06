my_dict = {'Igor': 20, 'Egor': 15, 'Oleg': 45}
print(f"Словарь: {my_dict}")
print(f"Имеющееся значение: {my_dict.get('Dima')}")
my_dict.update({'Serj': 22, 'Anna': 18})
not_exist = my_dict.pop('Egor')
print(f"Не имеющееся значение: {not_exist}")
print(f"Изменённый словарь: {my_dict}\n")

my_set = {1, 1, 1, 1, 2, 2, 2, 3, 3, 3}
print(f"Множество: {my_set}")
my_set.update({4, 4, 5, 5, 5})
my_set.discard(3)
print(f"Изменённое множество: {my_set}")