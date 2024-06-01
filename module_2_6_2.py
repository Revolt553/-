def print_params(a=1, b='строка', c=True):
    c = [1,2,3]
    print(a, b, c)

values_list = [1, True, 'ASD']
values_dict = {'a': 1, 'b': False, 'c': 'ASD'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3, "Good"]
print_params(*values_list_2, 42)
