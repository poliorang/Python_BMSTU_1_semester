## Егорова Полина, ИУ7-14б, лабораторная 11, базы данных
# имитация работы БД, создание бинарных файлов

import pickle

#проверка на int
def check_int(x):
    znaki = ['1','2','3','4','5','6','7','8','9','0']
    line = str(x)
    for i in line:
        if i not in znaki:
            return False
    return True

#проверка на положительный int, возвращает число
def plus_int(x):
    flag = check_int(x) and int(x) > 0
    while not flag:
        x = input('Должно быть введено натуральное число: ')
        flag = check_int(x) and int(x) > 0
    return int(x)

file = ''
point = -1
while point != '0':
    print('''
    0. Выход из программы
    1. Создание БД
    2. Добавление записи в БД
    3. Вывод БД
    4. Поиск записи БД по одному параметру
    5. Поиск записи БД по нескольким параметрам
    ''')
    point = input('Введите пункт меню: ')

    if point == '1':
        file = input('Введите название файла: ') + '.bin'
        count = input('Введите количество столбцов: ')
        while not plus_int(count):
            count = input('Должно быть введено натуральное число: ')
        count = int(count)
        column = []
        for i in range(count):
            column.append(input('Введите название столбца {}: '.format(i + 1)))
        with open(file, 'wb') as line:
            pickle.dump(column, line)
        print('База данных создана')

    if point == '2':
        while not file:
            file = input('Не выбрана БД. Введите название файла: ') + '.bin'
        try:
            with open(file, 'rb') as line:
                columns = pickle.load(line)
            dict = {}
            for col in columns:
                dict[col]= ''
            for col in columns:
                dict[col] = input('{}: '.format(col))
            with open(file, 'ab') as line:
                pickle.dump(dict, line)
        except pickle.UnpicklingError:
            print('БД повреждена')
        except:
            print('Выбрана несуществующая БД')
            file = ''

    if point == '3':
        while not file:
            file = input('Не выбрана БД. Введите название файла: ') + '.bin'
        try:
            print('\n')
            with open(file, 'rb') as line:
                columns = pickle.load(line)
                count = 0
                for col in columns:
                    print('{:^20}'.format(col), end='|')
                    count += 1
                print('\n' + '-' * 21 * count)
                try:
                    while True:
                        dict_current = pickle.load(line)
                        for col_current in dict_current:
                           print('{:^20}'.format(dict_current[col_current]), end='')
                        print()
                except:
                    pass
        except pickle.UnpicklingError:
            print('БД повреждена')
        except:
            print('Выбрана несуществующая БД')
            file = ''

    if point == '4':
        while not file:
            file = input('Не выбрана БД. Введите название файла: ') + '.bin'
        try:
            search_col = str(input('Введите название колонки, ко которой будет производиться поиск: '))
            search_word = str(input('Введите слово, по которому будет производиться поиск: '))
            with open(file, 'rb') as line:
                columns = pickle.load(line)
                count = 0
                search_num = 0
                for col in columns:
                    count += 1
                    if col == search_col:
                        search_num = count
                try:
                    print('\n')
                    shapka = False
                    while True:
                        dict_current = pickle.load(line)
                        count_1 = 0
                        for elem in dict_current:
                            count_1 += 1
                            if dict_current[elem] == search_word:
                                if count_1 == search_num:
                                    if not shapka:
                                        for col in columns:
                                            print('{:^20}'.format(col), end='')
                                            shapka = True
                                        print('\n', '-' * (21*count))
                                    for col in dict_current:
                                        print('{:^20}'.format(dict_current[col]), end='')
                                    print()
                except:
                    pass
        except pickle.UnpicklingError:
            print('БД повреждена')
            pass
        except:
            print('Выбрана несуществующая БД')
            file = ''

    if point == '5':
        while not file:
            file = input('Не выбрана БД. Введите название файла: ') + '.bin'
        try:
            search_col_1 = str(input('Введите название первой колонки, по которой будет производиться поиск: '))
            search_word_1 = str(input('Введите первое слово, по которому будет производиться поиск: '))
            search_col_2 = str(input('Введите название второй колонки, по которой будет производиться поиск: '))
            search_word_2 = str(input('Введите второе слово, по которому будет производиться поиск: '))
            with open(file, 'rb') as line:
                columns = pickle.load(line)
                count = 0
                search_num = 0
                for col in columns:
                    count += 1
                    if col == search_col_1:
                        search_num_1 = count
                    if col == search_col_2:
                        search_num_2 = count
                try:
                    shapka = False
                    print('\n')
                    while True:
                        dict_current = pickle.load(line)
                        count_1 = 0
                        for elem in dict_current:
                            count_1 += 1
                            if dict_current[elem] == search_word_1:
                                count_2 = 0
                                for elem_2 in dict_current:
                                    count_2 += 1
                                    if dict_current[elem_2] == search_word_2:
                                        if count_1 == search_num_1 and count_2 == search_num_2:
                                            if not shapka:
                                                for col in columns:
                                                    print('{:^20}'.format(col), end='')
                                                    shapka = True
                                                print('\n', '-' * (21*count))
                                            for col in dict_current:
                                                print('{:^20}'.format(dict_current[col]), end='')
                                            print()
                except:
                    pass
        except pickle.UnpicklingError:
            print('БД повреждена')
            pass
        except:
            print('Выбрана несуществующая БД')
            file = ''

print('Программа завершена')
