import io
from pprint import pprint

'''def custom_write(self, file_name, strings):
    self.file_name = open(file_name, 'a', encoding='utf-8')
    self.strings = strings[]'''


def custom_write(file_name, strings):
    file1 = open(file_name, 'w')
    tell_1_pos = file1.tell()
    file1.write(f'{strings[0]}\n')
    tell_2_pos = file1.tell()
    file1 = open(file_name, 'a', encoding='utf-8')
    file1.write(f'{strings[1]}\n')
    tell_3_pos = file1.tell()
    file1.write(f'{strings[2]}\n')
    tell_4_pos = file1.tell()
    file1.write(f'{strings[3]}')
    file1 = open(file_name, 'r', encoding='utf-8')
    # for index, line in enumerate(file1, 1): #попробовал получить номера строк
    #     print(index)
    file1.close()
    keys = [(1, tell_1_pos), (2, tell_2_pos), (3, tell_3_pos), (4, tell_4_pos)]
    strings_position = dict(zip(keys, strings))
    return strings_position
file_name = 'test.txt'
strings = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!',  'Спасибо!']

result = custom_write('test.txt', strings)


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
