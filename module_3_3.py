def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c,)
print_params()
values_list = 5, 'str', False
values_dict = {'a':3,'b':8,'c':10}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
