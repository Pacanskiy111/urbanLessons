def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    for i in strings:
        str_Number = strings.index(i) + 1
        byte_str_Number = file.tell()
        tup = str_Number, byte_str_Number
        strings_positions[tup] = i
        i += '\n'
        file.write(i)
        #print(strings_positions)
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)