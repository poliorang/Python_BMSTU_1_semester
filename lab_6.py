## Егорова Полина, ИУ7-14Б, лабораторная 6
# реализация меню, работа со списком, содержащим члены бесконечного ряда, буквы

#проверка на float
def check_float(x):
    znaki = ['1','2','3','4','5','6','7','8','9','-','+','0','e','.']
    line = str(x)
    num = len(line)

    flag = True
    for i in line: #проверка на допустимые знаки внутри строки
        if not (i in znaki):
            flag = False
    if flag:
        num_e = 0
        for i in line: #подсчет количества 'e' внутри строки
            if i == 'e':
                num_e += 1
        if num_e > 1: #если количество 'e' больше 1, то это строка
            flag = False
        if flag:
            num_t = 0
            for i in line: #подсчет количества '.' внутри строки
                if i == '.':
                    num_t += 1
            if num_t > 1: #если количество '.' больше 1, то это строка
                flag = False
            if flag: #если в строке есть 'e' делю ее на две, иначе не делю
                #если 'e' в строке нет
                if len(line) == 1 and (line[0] == '+' or line[0] == '-' or line[0] == '.'):
                    flag = False
                if flag:
                    if num_e == 0: #+ или - только на первом месте, если строки из одного символа знаков "+","-","." в ней быть не должно
                        for i in range(1,len(line)):
                            if line[i] == '+' or line[i] == '-':
                                flag = False
                    #если 'e' в строке есть, делю строку на две
                    elif num_e == 1:
                        if line.index('e') == 0 or line.index('e') == len(line)-1: #если "е" находится на краях строки
                            flag = False
                        if flag:
                            #если длина строки до или после "е" равна 1 и там находятся только символы "+","-","."
                            if (line.index('e') == 1 and (line[0] == '+' or line[0] == '-' or line[0] == '.'))\
                            or (line.index('e') == len(line) - 2 and (line[len(line) - 1] == '+' or line[len(line) - 1] == '-' or line[len(line) - 1] == '.')):
                                flag = False
                            if flag:
                                for i in range (line.index('e')): #проверка числа перед "е"
                                    #знаки "+","-" могут стоять только на первой позиции строки, точка - где угодно
                                    if i != 0 and (line[i] == '+' or line[i] == '-'):
                                        flag = False
                                    if flag:
                                        #в строкe справа от "е" точек быть не может, заки "+","-" могут находится только на первой позиции в строке 
                                        for i in range (line.index('e')+1, len(line)):
                                            if line[i] == '.' or (i>=line.index('e')+2 and(line[i] == '+' or line[i] == '-')):
                                                flag = False
                    else:
                        flag = False         
    return flag

#проверка на int
def check_int(x):
    znaki = ['1','2','3','4','5','6','7','8','9','0','-','+']
    flag = True
    line = str(x)
    if line == '-0' or line == '+0':
        return False
    for i in line:
        if i not in znaki:
            return False
    if flag:
        for i in range(1,len(line)):
            if line[i] == '+' or line[i] == '-':
                return False
    return True

#проверка на положительный int, возвращает число
def plus_int(x):
    flag = check_int(x) and int(x) > 0
    while not flag:
        x = input('Должно быть введено натуральное число: ')
        flag = check_int(x) and int(x) > 0
    return int(x)

#проверка на положительный int c нулем, возвращает число
def plus_int0(x):
    flag = check_int(x) and int(x) >= 0
    while not flag:
        x = input('Должно быть введено натуральное число или нуль: ')
        flag = check_int(x) and int(x) >= 0
    return int(x)

#состоит ли список из чисел
def check_chislo(x):
    flag = True
    for i in x:
        if check_float(i) == False:
            flag = False
            break
    return flag

#проверка на простое число
def check_prostoe(x):
    x = int(x)
    count = 2
    flag = False
    while x % count != 0 and count < x:
            count += 1
    if count == x:
        flag = True
    return flag

#проверка на то, сосит ли список только из гласных
def check_glas(x):
    line = str(x)
    znaki = ['a', 'e', 'o', 'i', 'u', 'y']
    flag = True
    for i in line:
        if i not in znaki:
            flag = False
    return flag


## начало программы

spisok = []
punkt = ['0','1','2','3','4','5','6','7']
print('Пункты меню:')
print('1. Проинициализировать список пeрвыми N элементами заданного ряда') # задан формулой бесконечного ряда
print('2. Добавить элемент в произвольное место списка')
print('3. Удалить произвольный элемент из списка')
print('4. Очистить список')
print('5. Найти значение К-го экстремума в списке, если он является списком чисел')
print('6. Найти наиболее длинную возрастающую последовательность простых чисел')
print('7. Найти последовательность, включающую в себя наибольшее количество строк, содержащих только гласные буквы')
print('0. Выход')

while True: #бесконечный цикл
    c = input('\nВыберите пункт меню: ')
    while c not in punkt:
        print('Недопустимый пункт меню')
        c = input('Выберите пункт меню: ')

    if c == '0': #пункт 0
        print('Выход из меню')
        break
    
    if c == '1': #пункт 1 
        k = plus_int(input('Введите количество элементов: '))
        spisok = [0] * k #создание списка 
        x = input('Введите x (|x| < 1): ')
        while check_float(x) != True or abs(float(x)) >= 1:
            x = input('Введите вещественный x (|x| < 1): ')
        x = float(x)
        #подсчет элементов списка по формуле бесконченого ряда
        print('Полученный список: ', end='')
        for i in range(k):
            if i == 0:
                spisok[i] = '1' #первый элемент всегда = 1
            else:
                spisok[i] = str((-x)**i) # формула бесконечного ряда
        print('Полученный список: ', end='')
        print(', '.join(spisok))

    if c == '2': #пункт 2
        if len(spisok) == 0:
            print('Список не задан')
        else:
            element = input('Введите новый элемент: ')
            index = plus_int0(input('Введите номер нового элемента: '))
            spisok.insert(index-1, element)
            print('Полученный список: ', end='')
            print(', '.join(spisok))

    if c == '3': #пункт 3
        if len(spisok) == 0:
            print('Список не задан')
        else:
            index = plus_int0(input('Введите номер удаляемого элемента: '))
            while abs(index-1) >= len(spisok):
                print('Список не содержит элемента с таким номером')
                index = check_int(input('Введите номер нового элемента: '))
            spisok.pop(index-1)
        print('Полученный список: ', end='')
        print(', '.join(spisok))

    if c == '4': #пункт 4 
        spisok.clear()
        print('Список очищен')

    if c == '5': #пункт 5
        if len(spisok) == 0:
            print('Список не задан')
        else:
            if check_chislo(spisok):
                count = 0
                num = plus_int(input('Введите номер экстремума: '))
                while num > len(spisok):
                    num = plus_int(input('Длина списка меньше введенного числа\nВведите другой номер экстремума: '))
                num = int(num)
                for i in range(1, (len(spisok)-1)):
                    if (float(spisok[i-1])<float(spisok[i])>float(spisok[i+1])) or (float(spisok[i+1])>float(spisok[i])<float(spisok[i-1])):
                        count += 1
                if count == num:
                    print('Значение {} экстремума: '.format(num), spisok[i])
                else:
                    print('Экстремум с данным номером не найден')
            else:
                print('Список не является списком чисел')

    if c == '6': #пункт 6
        if len(spisok) == 0:
            print('Список не задан')
        else:
            previous = i = count = 0
            countlist = [] #список, где будут храниться длины последовательностей
            firstlist = [] #список, где будут храниться индексы первых элементов последовательностей
            lastlist = [] #список, где будут храниться индексы последних элементов последовательностей
            while i != len(spisok):
                first = i
                #проверка, что элемент - число целое, простое и больше предыдущего
                while check_int(spisok[i]) and check_prostoe(spisok[i]) and int(spisok[i]) > previous:
                    previous = int(spisok[i])
                    count += 1
                    i += 1
                if i != first:
                    last = i
                    countlist.append(count)
                    firstlist.append(first)
                    lastlist.append(last)
                    count = 0
                    previous = 0
                    i -= 1
                i += 1
            if not countlist:
                print('Последовательность не найдена')
            else:
                m = countlist.index(max(countlist))
                print('Полученный список: ', end='')
                print(', '.join(spisok[firstlist[m]:lastlist[m]]))
            
    if c == '7': #пункт 7
        if len(spisok) == 0:
            print('Список не задан')
        else:
            i = count = 0
            countlist = [] #список, где будут храниться длины последовательностей
            firstlist = [] #список, где будут храниться первые элементы последовательностей
            lastlist = [] #список, где будут храниться последние элементы последовательностей
            while i != len(spisok):
                first = i
                #проверка, что элемент - строка, состоящая из гласных
                while not check_int(spisok[i]) and not check_float(spisok[i]) and check_glas(spisok[i]):
                    count += 1
                    i += 1
                if i != first:
                    last = i
                    countlist.append(count)
                    firstlist.append(first)
                    lastlist.append(last)
                    count = 0
                    previous = 0
                i += 1
            if not countlist:
                print('Последовательность не найдена')
            else:
                m = countlist.index(max(countlist))
                #инд. макс. элемента соотносится с инд. первого и последнего элемента этой посл. в соотв. списках
                print('Полученный список: ', end='')
                print(', '.join(spisok[firstlist[m]:lastlist[m]]))
                    
                    
    
        
