## Егорова Полина, ИУ7-14б, лабораторная 9, шифр Виженера

def alpha(line):  # проверка на наличие буквы в латинице
    flag = True
    alphabet = 'abcdefghijklmnopqrstuvwxyz ,.:;"!?'
    for simbol in line:
        if simbol not in alphabet:
            flag = False
    return flag


def check_menu(x):  # проверка на соответствие введенного знака допустимому пункту меню
    znaki = ['1', '2', '3', '4', '0']
    line = str(x)
    return line in znaki


print('Пункты меню: ')
print('1. Ввод строки')
print('2. Настройка шифрующего алгоритма (ввод ключ-слова)')
print('3. Шифрование строки с помощью шифра Виженера')
print('4. Расшифровка строки с помощью шифра Виженера')
print('0. Выход из программы')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
line = ''  # введенная строка
key = ''  # введенное ключ-слово
point = -1  # пункт меню
while point != 0:
    point = input('\nВведите пункт меню: ')
    while not check_menu(point):
        point = input('Недопустимое значение, повторите ввод пункта меню: ')
    point = int(point)

    if point == 1:  # пункт 1
        line = str(input('Введите строку: '))
        line = line.lower()  # приведение к нижнему регистру
        while not alpha(line):
            line = str(input('Строка должна содержать только символы латиницы: '))

    if point == 2:  # пункт 2
        key = str(input('Введите ключ-слово: '))
        key = key.lower()  # приведение к нижнему регистру
        while not alpha(key):
            key = str(input('Ключ должен содержать только символы латиницы: '))

    if point == 3:  # пункт 3
        # шифрование строки с помощью шифра Виженера
        if line == '' or key == '':
            print('Не введена строка или ключ, обратитесь к пунктам 1 и 2')
        else:
            string = str()  # будущая зашифрованная строка
            count = 0  # индекс текущей буквы ключа
            for simbol in line:
                if simbol in alphabet:  # если символ буквенный
                    cur_key = key[count]  # текущая буква ключа
                    pos_cur_key = alphabet.find(cur_key) + 1  # позиция текущей буквы ключа в алфавите
                    pos_cur_line = alphabet.find(simbol) + 1  # позиция текущея буквы строки в алфавите
                    el_num = int(pos_cur_key + pos_cur_line)  # позиция нового символа зашифрованной строки в алфавите
                    if el_num > 26:  # если номер позиции больше количества букв алфавита
                        el_num = el_num % 26
                    string += alphabet[el_num - 2]  # добаление нового символа в защифрованную строку
                    if count + 1 == len(key):  # пройдены все буквы ключ-слова, переход к первой
                        count = 0
                    else:  # переход к первой букве ключ-слова
                        count += 1
                else:  # если символ небуквенный
                    string += simbol
            print('Зашифрованная строка: ', string)

    if point == 4:  # пункт 4
        # расшифровывание строки с помощью шифра Виженера
        if line == '' or key == '':
            print('Не введена строка или ключ, обратитесь к пунктам 1 и 2')
        else:
            string = str()  # будущая расшифрованная строка
            count = 0  # индекс текущей буквы ключа
            for simbol in line:
                if simbol in alphabet:  # символ буквенный
                    cur_key = key[count]  # текущая буква ключа
                    pos_cur_key = alphabet.find(cur_key)  # позиция текущей буквы ключа в алфавите
                    pos_cur_line = alphabet.find(simbol)  # позиция текущея буквы зашифрованной строки в алфавите
                    el_num = int(pos_cur_line - pos_cur_key)  # позиция символа расшифрованной строки в алфавите
                    if el_num > 26:
                        el_num -= 26
                    string += alphabet[el_num]  # добаление нового символа в защифрованную строку
                    if count + 1 == len(key):  # пройдены все буквы ключ-слова, переход к первой
                        count = 0
                    else:  # перейти к первой буквы ключ-слова
                        count += 1
                else:  # небуквенный символ
                    string += simbol
            print('Расшифрованная строка: ', string)
print('Программа завершена')
