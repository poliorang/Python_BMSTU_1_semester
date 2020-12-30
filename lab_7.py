## Егорова Полина, ИУ7-14б, лабораторная 7, матрицы

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


## КАРТОЧКА 1

print('Карточка 1\n')

#ввод матрицы с клавиатуры
n = m = 6 #n строк, m столбцов
matrix_f = []
for line in range(n):
    cur_line = []
    print('Введите элементы строки {} через ENTER'.format(line))
    for el in range(m):
        element = input('{}. '.format(el))
        while not check_float(element):
            element = input('Должно быть введено вещественное число: ')
        cur_line.append(float(element))
    matrix_f.append(cur_line)

#вывод исходной матрицы
print('Исходная матрица:')
for line in matrix_f:
    for el in line:
        print('{:^7g}'.format(el), end='')
    print()
matrix_d = [[0 for j in range(m)] for i in range(n)] #нулевая матрица


#создание новой матрицы путем вычеркивания элементов диаг (5х6)
k1 = k2 = maximum = 0
#список, где будут храниться кол нулей для строки с соответствующим индексом
count = [0]*n 
print('\nВычеркнуть диагональные элементы, сдвиг по строке:')
for i in range(n):
    for j in range(m):
        if i != j != m: #не рассматривается диаг и m-ый элем 
            matrix_d[k1][k2] = matrix_f[i][j]
            if int(matrix_d[k1][k2]) == 0:
                count[i] += 1
            print('{:^7g}'.format(matrix_d[k1][k2]), end=' ')
            k2 += 1
    k2 = 0
    if k1 != n:
        k1 += 1
    print('')
    
maximum  = max(count)
if maximum == 0:
    print('Строки с нулевыми элементами не найдены')
else:
    print('Строка с максимальным количеством нулей: {}'.format(count.index(maximum) + 1))
    print('Количество нулевых элементов в строке {}: '.format(count.index(maximum) + 1), maximum)


##КАРТОЧКА 2
    
print('\nКарточка 2\n')

#ввод матрицы

n = m = 7 #n строк, m столбцов
matrix_b = []
for line in range(n):
    cur_line = []
    print('Введите элементы строки {} через ENTER'.format(line))
    for el in range(m):
        element = input('{}. '.format(el))
        while not check_float(element):
            element = input('Должно быть введено вещественное число: ')
        cur_line.append(float(element) )
    matrix_b.append(cur_line)
    
#вывод исходной матрицы
print('\nИсходная матрица:')
for line in matrix_b:
    for el in line:
        print('{:^7g}'.format(el), end='')
    print()

#замена диагонального элемента на минимальный для каждой строки
for i in range(n):
    mn = 0
    for j in range(m):
        if matrix_b[i][j] < matrix_b[i][mn]:
            mn = j  
    matrix_b[i][i], matrix_b[i][mn] = matrix_b[i][mn], matrix_b[i][i]

#вывод полученной матрицы
print('\nМин элемент строки поменять с диагональным:')
for line in matrix_b:
    for el in line:
        print('{:^7g}'.format(el), end='')
    print()


#создание новой матрицы путем вычеркивания эл диаг (7х6)
print('\nВычеркнуть диагональные элементы, сдвиг по столбцу:')
k1 = k2 = 0
matrix_a = [[0 for j in range(m)] for i in range(n)] #нулевая матрица
matrix_D = [] #новая матрица
for i in range(n):
    for j in range(m):
        if i != (n-1):
            if i >= j: #если номер столбца больше/равен номера строки
                matrix_a[k1][k2] = matrix_b[i+1][j]
            else: #если номер столбца меньше номера строки
                matrix_a[k1][k2] = matrix_b[i][j]
            if matrix_a[k1][k2] > 0:
                matrix_D.append(str(matrix_a[k1][k2]))
            print('{:^7g}'.format(matrix_a[k1][k2]), end='')
        k2 += 1
    k2= 0
    if k1 != n:
        k1 += 1
    print('')

#вывод положительных элементов матрицы 
print('\nПоложительные элементы матрицы: ')
print(', '.join(matrix_D))


       
