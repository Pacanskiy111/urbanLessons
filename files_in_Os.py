import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(os.getcwd(), file)
        filetime = os.path.getmtime('files_in_Os.py')
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        filesize = os.path.getsize('files_in_Os.py')
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, \n'
              f'Путь: {filepath}, \n'
              f'Размер: {filesize} байт, \n'
              f'Время изменения: {formatted_time}, \n'
              f'Родительская директория: {parent_dir}')