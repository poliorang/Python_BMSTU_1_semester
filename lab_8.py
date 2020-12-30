## Егорова Полина, ИУ7-14б, лабораторная 8, интегралы
# вычисление интегралов методов Буля и методом трапеций
# вычисление интеграла методом трапеций с заданной точностью
# вычисление абсолютной и относительной ошибки для метода трапеций

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

#проверка на положительный int, кратный 4, возвращает число
def plus4_int(x):
    flag = check_int(x) and int(x) > 0 and int(x) % 4 == 0
    while not flag:
        x = input('Должно быть введено натуральное число, кратное 4: ')
        flag = check_int(x) and int(x) > 0 and int(x) % 4 == 0
    return int(x)

#задание функции
def function_x(x):
    f = x*x
    return f

a = input('Введите начало отрезка: ')
while check_float(a) == False:
    a = input('Должно быть введено вещественное число: ')
b = input('Введите конец отрезка: ')
while check_float(b) == False:
    b = input('Должно быть введено вещественное число: ')
a = float(a)
b = float(b)
if a > b:
    a, b = b, a
n1 = plus4_int(input('Введите количество разбиений n1, кратное 4: '))
n2 = plus4_int(input('Введите количество разбиений n2, кратное 4: '))

# рассчет интеграла методом Буля
def bool_method(n, a, b):
    step = (b - a) / n
    sum7 = sum32 = sum12 = 0 
    for i in range(1, (n // 4) + 1):
        #рассчет слагаемых, умножаемых на 7 
        sum7 = sum7 + function_x(a + step * (4 * i - 4)) + function_x(a + step * 4 * i)
        #рассчет слагаемых, умножаемых на 32
        sum32 = sum32 + function_x(a + step * (4 * i - 3)) + function_x(a + step * (4 * i - 1))
        #рассчет слагаемых, умножаемых на 12
        sum12 += function_x(a + step * (4 * i - 2))
    bool_int = abs((sum7 * 7 + sum32 * 32 + sum12 * 12) * 2 * step / 45)
    return bool_int

# рассчет интеграла методом трапеций
def trapeze_method(n, a, b):
    step = (b - a) / n
    sum1 = 0
    for i in range(1, n):
        sum1 += function_x(a + i * step)
    trapeze_int = abs((step / 2) * (function_x(a) + function_x(b) + 2 * sum1))
    return trapeze_int

#рассчет интеграла методом трапеций с заданной точностью
eps = input('\nВведите точность: ')
while not check_float(eps):
    eps = input('Должно быть введено вещественное число: ')
eps = float(eps)

def epsi(n, a, b, eps):
    n_for_eps1 = n
    n_for_eps2 = n*2
    while abs(trapeze_method(n_for_eps2, a, b) - trapeze_method(n_for_eps1, a, b)) > eps:
        n_for_eps1 = n_for_eps2
        n_for_eps2 = n*2
    trap_eps = abs(trapeze_method(n_for_eps2, a, b))
    return trap_eps

#рассчет интеграла для входных значений n для каждого метода
bool_1 = bool_method(n1, a, b) #метод Буля, n1
bool_2 = bool_method(n2, a, b) #метод Буля, n2
trap_1 = trapeze_method(n1, a, b) #метод трапеций, n1
trap_2 = trapeze_method(n2, a, b) #метод трапеций, n2
trap_eps_1 = epsi(n1, a, b, eps) #метод трапеций с точностью, n1
trap_eps_2 = epsi(n2, a, b, eps) #метод трапеций с точностью, n2

#вычисление абсолютной ошибки (метод трапеций)
error_abs = abs(trap_eps_1 - trap_eps_2)
#вычсиление относительной ошибки (метод трапеций)
error_otn = abs((trap_eps_2 - trap_eps_1) / trap_eps_2)

print('\n  Метод   |    n1 = {:<7.7g}|    n2 = {:<7.7g}|'.format(n1, n2))
print('__________|________________|________________|')
print('   Буля   |{:^16.7g}|{:^16.7g}|'.format(bool_1, bool_2))
print(' Трапеций |{:^16.7g}|{:^16.7g}|'.format(trap_1, trap_2))
print('__________|________________|________________|\n')
print('Метод трапеций с точностью {:g} для {:.7g} разбиений: {:.7g}'.format(eps, n1, trap_eps_1))
print('Метод трапеций с точностью {:g} для {:.7g} разбиений: {:.7g}'.format(eps, n2, trap_eps_2))
print('\nАбсолютная ошибка при вычислении интеграла методом трапеций для {:g} разбиений: {:.7f}'.format(n1, error_abs))
print('Относительная ошибка при вычислении интеграла методом трапеций для {:g} разбиений: {:.7f}'.format(n1, error_otn))
