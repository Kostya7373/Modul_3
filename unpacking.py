

def print_params ( a = 1, b = 'строка', c = True):
    print('a =', a, 'b=', b, 'c=', c)

print_params()
print_params(b = 123) # выдает замечание ( b должно быть строкой)
print_params(b =1, c = 'крот', a=23) # выдает замечание ( b должно быть строкой) (с должно быть bool)
print() # пустой принт для разделения строк при выводе ответа

print_params(b = 'camel')
print_params(a=[1,2,3])
print()

values_list = (1, 'kot', True)
values_dict = {'a': 3, 'b' : 4 , 'c' : 5 } # Если имена ключей не соответствуют параметрам, то будет ошибка


print_params( values_list ) # передает в параметр (а)
print_params( values_dict )# передает в параметр (а)
print()

print_params(*values_list ) # передает в параметр (а)
print_params( **values_dict ) # передает в параметр (а)
print()

values_list_2 =[54.32, 'Строка' ]
print_params(*values_list_2, 42) # (а) уходит в (с) так как находится, на последнем месте

