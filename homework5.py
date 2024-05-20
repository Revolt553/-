my_list = ['яблоко', 'груша', 'апельсин', 'персик', 'лимон', 'манго']
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[2:5])
my_list[2] = 'дыня'
print(my_list)

my_dict = {'яблоко':'apple', 'груша':'pear', 'апельсин':'orange', 'персик':'peach',
           'лимон':'lemon', 'манго':'mango'}
print(my_dict)
print(my_dict.get('персик'))
my_dict['груша'] = 'PEAR'
print(my_dict)