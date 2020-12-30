## Егорова Полина, ИУ7-14б, лабораторная 10, текст
# реализация меню, работа с текстом
# 6 пункт - вычленение и подсчет арифметических выражений 

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
consonant = 'бвгджзйклмнпрстфхцчшщъь'  # согласные буквы
vowel = 'аеоэюяи'  # гласные буквы
separators = ['.', '!', '?'] # разделители
operations = ['^', '*', '/', '%', '+', '-', 'sqrt', '(', ')', '=']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

def check_menu(x): # проверка на соответствие введенного знака допустимому пункту меню
    line = str(x)
    return line in numbers

def alpha(line): # проверка на наличие буквы в русском алфавите
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    for simbol in line:
        if simbol not in alphabet:
            return False
    return True

### не используется ###
def centering(m_): # перекомпановка: по 1 предложению в каждой строке
    count_point = 0 # количество точек
    for i in range(len(m_)):
        count_point += str(m_[i]).count('.') + str(m_[i]).count('!') + str(m_[i]).count('?')
    m_new = [0]*count_point
    ind = 0
    cur_sentense = ''  # текущее предложение
    for sentense in m_:
        for j in range(len(sentense)):
            if sentense[j] not in separators:
                if sentense[j] == ' ':
                    while sentense[j-1] == ' ' and sentense[j+1] == ' ':
                            j += 1
                cur_sentense += sentense[j]
            else:
                m_new[ind] = cur_sentense.lstrip()
                ind += 1
                cur_sentense = ''
    m_ = m_new
    return m_

def max_len(m_): # определение максимальной длины предложения в тексте
    maximum = 0
    for i in range(len(m_)):
        if len(m_[i]) > maximum:
            maximum = len(m_[i])
    return maximum

def oper_and_num(line): # проверка на то, что выражение содержит и цифры, и знаки операций
    oper = num = False
    for simbol in line:
        if simbol in operations:
            oper = True
        if simbol in numbers:
            num = True
    if oper and num:
        return True
    else:
        return False

def n_find(line, simbol, n): # индекс n вхождения символа в строку
    n_current = i = 0
    while n_current != n and i < len(line):
        if line[i] == simbol:
            n_current += 1
        i += 1
    if n_current == n:
        return i - 1
    else:
        return -1

def counting(line): # счет
    for i in range(len(line)):
        if line[i] == '*':
            return str(float(line[:i]) * float(line[i+1:]))
        elif line[i] == '+':
            return str(float(line[:i]) + float(line[i+1:]))
        elif line[i] == '-':
            return str(float(line[:i]) - float(line[i+1:]))
        elif line[i] == '%':
            return str(float(line[:i]) % float(line[i+1:]))
        elif line[i] == '^':
            return str(float(line[:i]) ** float(line[i+1:]))
        elif line[i] == '/' and line[i+1] != '/':
            return str(float(line[:i]) / float(line[i+1:]))
        elif line[i] == line[i+1] == '/':
            return str(float(line[:i]) // float(line[i+2:]))

def parenthesis(math):  # расстановка скобок в выражении, не содержащем скобки
    bracket = 0
    for ind_oper in range(7):  # индекс операции в списке операций
        while operations[ind_oper] in math:  # если операция содержится в выражении
            plus = 1  # если операция состоит из одного знака
            if ind_oper == 2:  # если идет рассчет вхождения третьего символа списка операций (/)
                if '/' in math:
                    ind = math.index(operations[ind_oper])  # индекс знака операции
                    if math[ind + 1] == '/':
                        plus = 2  # если операция состоит из двух знаков
                else:
                    continue
            j = math.index(operations[ind_oper]) + plus  # индекс элемента, справа от операции
            if math[j] == '(' and math[j - 2] == ')':
                math = math[:j - 1] + '$' + math[j:]
                j_1 = j + 1
                num = 1 # количество открытых на текущй момент скобок
                while num != 0:
                    while math[j_1] != ')':
                        if math[j_1] == '(':
                            num += 1
                        j_1 += 1
                    j_1 += 1
                    num -= 1
                math = math[:j_1] + ')' + math[j_1:]
                j_1 = j - 3
                num = 1 # количество открытых на текущй момент скобок
                while num != 0:
                    while math[j_1] != '(':
                        if math[j_1] == ')':
                            num += 1
                        j_1 -= 1
                    j_1 -= 1
                    num -= 1
                math = math[:j_1] + '(' + math[j_1:]
            else:
                while math[j] in numbers or math[j] == '(':
                    if math[j] == '(':
                        while math[j] != ')':
                            j += 1
                        j += 1
                    if math[j] in numbers:
                        j += 1
                math = math[:j] + ')' + math[j:]
                bracket += 1
                j = math.index(operations[ind_oper]) - 1
                bracket_cur = math[:j].count('(')
                while math[j] in numbers or math[j] == ')':
                    if math[j] == ')':
                        for z in range(bracket_cur):
                            while math[j] != '(':
                                j -= 1
                            j -= 1
                    if math[j] in numbers:
                        j -= 1
                math = math[:j + 1] + '(' + math[j + 1:]
                j = math.index(operations[ind_oper])
                math = math[:j] + ('$' * plus) + math[j + plus:]
                bracket += 1
        math = math.replace('$', operations[ind_oper])
    return math.replace(' ', '')

def counting_operation(math):
    count_oper = 0
    for sim in range(len(math)):
        if math[sim] in operations[:6]:
            if math[sim] == operations[2] and math[sim + 1] == operations[2]:
                count_oper += 1
                sim += 1
            else:
                count_oper += 1
    return count_oper


# создание массива с цитатами из романа "Мастер и Маргарита"
m_and_m = ['33 Все будет  3+5-3*5 правильно, 2 3^2+4+2 на этом ',
            'построен мир    5*(4+5*67)*4 мир. Злых 1^2//3//4людей нет на свете, есть',
            'только люди 6*78/8несчастливые. Да. 2^2+1^0+14/7 Аннушка 10/2/2^3уже',
            'купила подсолнечное масло, 4^5+(7/2+4) и не 7*9//3 только купила, но даже разлила.'
            'Зачем же 7^(2+6)-1 гнаться по',' следам',
            'того, что 45 уже, 4%4    2^6-7/2 окончено! Факт – 40//5*4//2-7 самая упрямая',
            'в мире вещь?    (6+1^7)*7^5-4 Оскорбление 4*5+8^2является обычной наградой за хорошую работу.']

print('Пункты меню: ')
print('0. Выход из программы')
print('1. Выравнивание текста по левому краю')
print('2. Выравнивание текста по правому краю')
print('3. Выравнивание текста по ширине')
print('4. Удаление заданного слова')
print('5. Замена одного слова другим во всем тексте')
print('6. Подсчет арифметических выражений')
print('7. Поиск предложения с максимальным количеством слов, где согласная чередуется с гласной')
print('8. Поиск предложения, содержащего слово с максимальным количеством согласных букв')
print('9. Поиск предложения, содержащего максимальное количество слов, начинающихся на заданную букву')

# m_and_m = centering(m_and_m)

point = -1
while point != 0:
    point = input('\nВведите пункт меню: ')
    while not check_menu(point):
        point = input('Недопустимое значение, повторите ввод пункта меню: ')
    point = int(point)

    if point == 1:
        for i in range(len(m_and_m)): # удаление пробелов в начале и в конце строки
            m_and_m[i] = str(m_and_m[i]).strip()
        if m_and_m[1][1] == m_and_m[1][2] == ' ':
            for i in range(len(m_and_m)):
                m_and_m[i] = str(m_and_m[i]).lstrip()
                print(m_and_m[i])
        else: # если уже была применена команда 3 пункта
            for i in range(len(m_and_m)):
                length_1 = len(m_and_m[i])
                j = 0
                while j < length_1:
                    if m_and_m[i][j] == ' ':
                        while m_and_m[i][j+1] == ' ':
                            m_and_m[i] = m_and_m[i][:j+1] + m_and_m[i][j+2:]
                            length_1 -= 1
                    j += 1
                print(m_and_m[i])


    if point == 2:
        for i in range(len(m_and_m)): # удаление пробелов в начале и в конце строки
            m_and_m[i] = str(m_and_m[i]).strip()
        width = max_len(m_and_m) # длина максимального предложения в тексте
        if m_and_m[1][str(m_and_m[1]).find(m_and_m[1][1]) + len(m_and_m[1][1]) + 3] != ' ':
            for i in range(len(m_and_m)):
                m_and_m[i] = (width - len(m_and_m[i])) * ' ' + m_and_m[i]
                print(m_and_m[i])
        else:
            for i in range(len(m_and_m)):
                length_1 = len(m_and_m[i])
                j = 0
                while j < length_1:
                    if m_and_m[i][j] == ' ':
                        while m_and_m[i][j+1] == ' ':
                            m_and_m[i] = m_and_m[i][:j+1] + m_and_m[i][j+2:]
                            length_1 -= 1
                    j += 1
                m_and_m[i] = (width - len(m_and_m[i])) * ' ' + m_and_m[i]
                print(m_and_m[i])


    if point == 3:
        for i in range(len(m_and_m)): # удаление пробелов в начале и в конце строки
            m_and_m[i] = str(m_and_m[i]).strip()
        width = max_len(m_and_m)
        for i in range(len(m_and_m)):
            m_and_m[i] = str(m_and_m[i]).lstrip()
            count = 0  # счетчик всех символов, кроме пробела
            whitespace_count = 0  # счетчик пробелов
            sentense_new = '' # новая строка
            if ' ' not in m_and_m[i]:
                sentense_new = m_and_m[i]
            else:
                for simbol in m_and_m[i]:
                    if simbol != ' ':  # если символ не являестя пробелом
                        count += 1
                    else:  # если символ является пробелом
                        whitespace_count += 1
                whitespace = (width - count) // whitespace_count  # количество повторений пробелов между словами
                last = width - count - (whitespace * whitespace_count)  # + whitespace нераспределенные пробелы
                for simbol in m_and_m[i]:
                    if simbol != ' ': # если символ не являестя пробелом
                        sentense_new += simbol
                    else: # если символ является пробелом
                        whitespace_count -= 1
                        if last != 0:
                            sentense_new += ' ' * (whitespace + 1)
                            last -= 1
                        else:
                            sentense_new += ' ' * whitespace
            m_and_m[i] = sentense_new
            print(m_and_m[i])


    if point == 4:
        word = (input('Введите слово, которое нужно удалить: ').lower())
        while not alpha(word):
            word = (input('Слово должно содержать только буквы русского алфавита, повторите ввод: ')).lower()
        check = False
        for sent in range(len(m_and_m)):
            sentense = sentense_new = ' ' + m_and_m[sent] + ' ' # добавление пробелов справа и слева
            k = sentense.lower().count(word) # количество вхождений слова в строку
            for ind in range(k):
                i = sentense.lower().find(word) - 1
                j = sentense.lower().find(word) + len(word)
                if sentense[i] not in alphabet and sentense[j] not in alphabet:
                    check = True
                    if sentense[j] == ' ':
                        sentense = sentense[:i] + sentense[j:]
                    else:
                        sentense = sentense[:i] + sentense[j+1:]
                else:
                    sentense = sentense[:i+1] + '$' * len(word) + sentense[j:]
            sentense = sentense.replace('$' * len(word), word)
            m_and_m[sent] = sentense[1:-1]
            print(m_and_m[sent])
        if not check:
           print('\nДанного слова нет в тексте')


    if point == 5:
        word_del = (input('Введите слово, которое нужно заменить: ')).lower()
        while not alpha(word_del):
            word_del = (input('Слово должно содержать только буквы русского алфавита, повторите ввод: ')).lower()
        word_new = input('Введите слово, на которое будет заменено удаленное: ')
        while not alpha(word_new):
            word_new = input('Слово должно содержать только буквы русского алфавита, повторите ввод: ')
        check = False
        for sent in range(len(m_and_m)):
            sentense = ' ' + m_and_m[sent] + ' '  # добавление пробелов справа и слева
            k = sentense.lower().count(word_del)  # количество вхождений слова в строку
            for ind in range(k):
                i = sentense.lower().find(word_del) - 1
                j = sentense.lower().find(word_del) + len(word_del)
                if sentense[i] not in alphabet and sentense[j] not in alphabet:
                    check = True
                    sentense = (sentense[:i+1] + word_new + sentense[j:])
                else:
                    sentense = sentense[:i+1] + '$' * len(word_del) + sentense[j:]
            sentense = sentense.replace('$' * len(word_del), word_del)
            m_and_m[sent] = sentense[1:-1]
            print(m_and_m[sent])
        if not check:
            print('\nВведенного удаляемого слова нет в тексте')


    if point == 7:
        count = [0]*len(m_and_m) # массив, где будет храниться количество подходящих слов для каждой строки
        check = '0'
        for ind in range(len(m_and_m)):
            sentense = str(m_and_m[ind]).lower() + ' '
            length_1 = 0 # фактическая длина слова
            length_2 = 0 # длина последовательности чередующих согласных и гласных в слове
            for simbol in sentense:
                if simbol in alphabet:
                    length_1 += 1
                    if simbol in vowel and check != 'v':
                        check = 'v'
                        length_2 += 1
                    if simbol in consonant and check != 'c':
                        check = 'c'
                        length_2 += 1
                else:
                    if length_1 == length_2:
                        count[ind] += 1
                    length_1 = length_2 = 0
                    check = '0'
        print('Предложение с максимальным количеством слов, где согласная чередуется с гласной:\n', \
              m_and_m[count.index(max(count))])


    if point == 8:
        max_consonant = 0 # длина слова, содержащего макс кол-во согласных букв
        num = -1 # номер предложения, содержащего слово с макс кол-вом согласных букв
        for sent in range(len(m_and_m)):
            current_len = 0
            sentense = str(m_and_m[sent]).lower() + ' '
            for simbol in sentense:
                if simbol in alphabet:
                    if simbol in consonant:
                        current_len += 1 # количество согласных в слове
                else:
                    if current_len > max_consonant: # если кол-во согласных в данном слове больше, чем в найденном ранее
                        max_consonant = current_len # длина слова, содержащего макс кол-во согласных букв
                        num = sent # номер предложения, содержащего слово с макс кол-вом согласных букв
                        current_len = 0
        if num != -1:
            print('Предложение, содержащее слово с максимальным количеством согласных букв:\n', m_and_m[num])
        else:
            print('В тексте нет слов, содержащих согласные')


    if point == 9:
        character = input('Введите букву: ')
        while not alpha(character) or len(character) > 1:
            character = input('Недопустимый символ. Повторите ввод: ')
        max_count = 0 # максимальное количество слов на заданную букву в предложении
        num = -1
        for sent in range(len(m_and_m)):
            current_count = 0  # текущее количество слов на заданную букву в предложении
            sentense = ' ' + str(m_and_m[sent]).lower()
            for i in range(1, len(sentense)-1):
                if sentense[i-1] == ' ' and sentense[i] != ' ':
                    if sentense[i] == character:
                        current_count += 1
            if current_count > max_count:
                max_count = current_count
                num = sent
        if num != -1:
            print('Предложение, содержащее максимальное количество слов, начинающихся на заданную букву: \n', m_and_m[num])
        else:
            print('Текст не содержит слов, начинающихся на букву {}'.format(character))


    if point == 6:

        # вычленение арифметических выражений
        math = [''] * 1000
        mathematics = [] # будущий список арифметических выражение
        ind = 0
        for i in range(len(m_and_m)):
            sentense = m_and_m[i]
            j = 0
            while j < len(sentense) - 1:
                if sentense[j] in operations or sentense[j] in numbers:
                    j_1 = j + 1
                    math[ind] += sentense[j] # добавление элемента строки в текущее выражение
                    while sentense[j_1] in operations or sentense[j_1] in numbers:
                        math[ind] += sentense[j_1] # добавление элемента строки в текущее выражение
                        j_1 += 1
                        # sentense_2 = sentense_2[:j_1-1] + '&' + sentense_2[j_1:]
                    ind += 1
                    j = j_1
                j += 1
                ind += 1
        for i in range(len(math)): # если строка не число или знак операции, а выражение
            if math[i] != 0 and oper_and_num(math[i]):
                mathematics.append(math[i])
        mathematics_1 = mathematics.copy()
        mathematics_2 = mathematics.copy()

        # подсчёт выражения
        for i in range(len(mathematics)):
            math = '  '+ mathematics[i] + '  ' # текущее выражение
            math_prev = math_next = ''
            count_bracket = math.count('(') # количество скобок в выражении / 2
            # если в исходном выражении нет скобок
            if count_bracket == 0:
                bracket = 0
                math = parenthesis(math)
                math = math.replace(' ', '')
                mathematics[i] = math
                count_bracket_cur = math.count('(') # количество скобок в получившейся строке / 2

                #подсчет скобок
                while count_bracket_cur != 0:
                    bracket_ind_l = n_find(math, '(', count_bracket_cur)  # индекс вхождения '(' в строку
                    bracket_ind_r = bracket_ind_l
                    while math[bracket_ind_r] != ')': # индекс вхождения ')' в строку
                        bracket_ind_r += 1
                    math_new = math[bracket_ind_l+1:bracket_ind_r]
                    math_new = counting(math_new)
                    math = math[:bracket_ind_l] + math_new + math[bracket_ind_r + 1:]
                    count_bracket_cur -= 1
                mathematics_1[i] = math
                continue
            else:
                count_bracket += 1
                math = '(' + math + ')'
                while count_bracket != 0:
                    bracket_ind_l = n_find(math, '(', count_bracket) # индекс вхождения '(' в строку
                    bracket_ind_r = bracket_ind_l
                    while math[bracket_ind_r] != ')': # индекс вхождения ')' в строку
                        bracket_ind_r += 1
                    math_new = '  ' + math[bracket_ind_l+1:bracket_ind_r] + '  '
                    math_new = parenthesis(math_new)
                    count_bracket += 1
                    math = str(math[:bracket_ind_l] + math_new.replace(' ', '') + math[bracket_ind_r+1:]).replace(' ', '')
                    count_bracket -= 1
                    count_operation = 0 # количество знаков операций с выражении
                    count_bracket_cur = math.count('(')
                    while count_bracket_cur != 0: # пока количество скобок не 0
                        bracket_ind_l = n_find(math, '(', count_bracket_cur)  # индекс вхождения '(' в строку
                        bracket_ind_r = bracket_ind_l
                        while math[bracket_ind_r] != ')':  # индекс вхождения ')' в строку
                            bracket_ind_r += 1
                        math_new = math[bracket_ind_l + 1:bracket_ind_r]
                        count_oper = counting_operation(math_new)
                        if count_oper != 1: # если больше 1 операции
                            math_new = parenthesis(str(' ' + math_new + ' '))
                            count_oper = counting_operation(math_new)
                            count_bracket = math_new.count('(')
                            math = math_new
                            break
                        else:
                            math_new = counting(math_new)
                            math = math[:bracket_ind_l] + math_new + math[bracket_ind_r + 1:]
                            count_bracket_cur -= 1
                            count_oper = counting_operation(math)
                    math = math
                    if not oper_and_num(math):
                        break
            mathematics_1[i] = math
        for i in range(len(mathematics)):
            print('{}. '.format(i+1), mathematics_2[i], '=', mathematics_1[i])
print('Программа завершена')
