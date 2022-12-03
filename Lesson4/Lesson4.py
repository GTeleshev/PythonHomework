# 1. Вычислить число Pi c заданной точностью *d*
# *Пример:*
# - при d = 0.001, π = 3.141

print('Задача 1. Вычислить число Pi c заданной точностью *d*')


def pi_calc_precision(precision=0.001):
    pi_out = 3.0
    sign = 1
    i = 1
    add1 = 0.1
    add2 = 0
    while ((add2 - add1) ** 2) ** 0.05 > precision:
        add1 = add2
        double_i = 2 * i
        seq = 4 / (double_i * (double_i + 1) * (double_i + 2)) * sign
        add2 = add2 + seq
        sign = sign * (-1)
        i += 1
    out_put_string = f"Число пи с точностью до {precision}: {pi_out + add2}, количество итераций: {i}"
    return out_put_string


d = float(input("Введите точность вычисления числа пи: "))
print(pi_calc_precision(d))

# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# 24 -> 2 2 2 3

print('Задача 2. Список простых множителей числа N')


def prime_factors(num):
    i = 2
    prime_factor_list = []
    while i * i <= num:
        while num % i == 0:
            prime_factor_list.append(i)
            num = num / i
        i += 1
    if num > 1:
        prime_factor_list.append(num)
    return prime_factor_list


n = int(input("Введите число: "))
print(prime_factors(n))

# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
# [1, 1, 1, 2, 2, 3, 5, 4, 4, 7, 8, 8, 7] -> [3, 5]

print('Задача 3. Вывод список неповторяющихся элементов последовательности')

list_1 = [1, 1, 1, 2, 2, 3, 5, 4, 4, 7, 8, 8, 7, 13, 11, 10, 78]


def unique_elements(lst):
    instance_count = [0] * len(lst)
    unique_list = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                instance_count[i] += 1
        if instance_count[i] < 2:
            unique_list.append(lst[i])
    return unique_list


print(list_1)
print(unique_elements(list_1))

# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# *Пример:*
# - k=3 => 2*x**3 + 2*x**2 + 4*x + 5 = 0 или x**3 + 5 = 0 или 10*x**2 = 0
print('Задача 4. Генерация и запись многочлена')
from random import randint


def gen_polynomial_dict(pow, min_coeff, max_coeff):
    pol_dict = {}
    for k in range(pow, -1, -1):
        pol_dict[k] = randint(min_coeff, max_coeff)
    return pol_dict


def print_polynomial(pol_dict):
    output_string = ""
    string = "-"
    pow = max(pol_dict.keys())
    for i in pol_dict.keys():
        coeff = pol_dict[i]
        if coeff < 0 and i != 0:
            string = f"{coeff}*x**{i}"
            output_string += string
        elif coeff > 0 and i < pow and i != 0:
            string = f"+{coeff}*x**{i}"
            output_string += string
        elif i == 0 and coeff > 0:
            string = f"+{coeff}"
            output_string += string
        elif i == 0 and coeff < 0:
            string = f"{coeff}"
            output_string += string
        elif coeff > 0 and i == pow:
            string = f"{coeff}*x**{i}"
            output_string += string
    return output_string


rec = int(input("Введите максимальную степень многочлена: "))
pol1 = gen_polynomial_dict(rec, -100, 100)
pol2 = gen_polynomial_dict(rec, -100, 100)
polstring1 = print_polynomial(pol1)
polstring2 = print_polynomial(pol2)

print(polstring1)

with open('polynom1', 'w') as pol_file1:
    pol_file1.write(polstring1)

with open('polynom2', 'w') as pol_file2:
    pol_file2.write(polstring2)

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

print('Задача 5. Сформировать файл, содержащий сумму многочленов')


# делит строку на отдельные блоки между знаками (+ / -)
def pol_spl(string):
    stringlist = []
    sl = len(string)
    newpos = 0
    for k in range(1, sl):
        if string[k] == "+" or string[k] == "-" and k != sl - 1:
            stringlist.append(string[newpos:k])
            newpos = k
        elif string[k] == "+" or string[k] == "-" or k == sl - 1:
            stringlist.append(string[newpos:k] + string[k])
    return stringlist


# обрабатывает отдельные блоки между знаками (+/-), выделяет степень и коэффициент
def block_parse(block, sym):
    bl = len(block)
    pnum = []
    posx = block.find(sym)
    if posx != -1 and posx != bl - 1:
        pnum.append(int(block[posx + 1:bl]))
        pnum.append(int(block[0:posx]))
    elif posx == bl - 1:
        pnum.append(1)
        pnum.append(int(block[0:bl - 1]))
    else:
        pnum.append(0)
        pnum.append(int(block[0:bl - 1]))
    return pnum


# форматирует многочлен в словарь в виде степень / коэффициент
def poly_to_dict(pol_string):
    pol_out = {}
    clean_pol = pol_string.replace("*", "")
    clean_pol = clean_pol.replace("+x", "+1x")
    clean_pol = clean_pol.replace("-x", "-1x")
    pol_list = pol_spl(clean_pol)
    for k in pol_list:
        block = block_parse(k, "x")
        pol_out[block[0]] = block[1]
    return pol_out


# суммирует два полинома (словаря)
def sum_poly(poly1: dict, poly2: dict):
    res_dict = poly1.copy()
    res_dict.update(poly2)
    for k in res_dict.keys():
        res_dict[k] = poly1[k] + poly2[k]
    return res_dict


# чтение строк

polynomial1 = open('polynom1', 'r').readline()
polynomial2 = open('polynom2', 'r').readline()

# генерация словарей

pol1 = poly_to_dict(polynomial1)
pol2 = poly_to_dict(polynomial2)

# преобразование словарей в строки

polstring1 = print_polynomial(pol1)
polstring2 = print_polynomial(pol2)

# суммирование словарей, генерация результируюшего многочлена

sumpol = sum_poly(poly_to_dict(polynomial1), poly_to_dict(polynomial2))
sumstring = print_polynomial(sumpol)

# вывод в консоль

print("Многочлен 1", polstring1)
print("Многочлен 2", polstring2)
print("Сумма многочленов", sumstring)

# запись в файл

with open('sumpol', 'w') as pol_file2:
    pol_file2.write(sumstring)

