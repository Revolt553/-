def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_position = {}
    for index, string in enumerate(strings, start=1):
        file.write(string + '\n')
        position = file.tell()
        strings_position[(index, position)] = string
    file.close()
    return strings_position
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
