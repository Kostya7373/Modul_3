# Задача "Счётчик вызовов"

# Задача "Счётчик вызовов"
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    print([len(string), string.upper(), string.lower()])


def is_contains(string, list_):
    count_calls()
    list_1 = [] # создаем новый список для элементов в одном регистре
    for a in range(len(list_)): # переебираем  список
        d = (list_[a]).upper() #  Переводим в один регистр
        list_1.append(d)
    print(string.upper() in list_1 ) # (Проверяем наличие элемента (string)  списке (list_1)


string_info('Capibara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print('Ва сделали ', calls, 'запросов')

