# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# *Пример:*
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#
print('Задача 1. Сумма элементов списка, стоящих на нечётной позиции')

num_list = [2, 3, 5, 9, 3]
print('Список: ', num_list)

def odd_sum(numlist):
    sum = 0
    for i in range(1, len(numlist), 2):
        sum = sum + numlist[i]
    return sum


print('Сумма элементов на нечётных позициях: ', odd_sum(num_list))

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# *Пример:*
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
#

print('Задача 2: Напишите программу, которая найдёт произведение пар чисел списка')

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]
print('Список 1: ', list1)
print('Список 2: ', list2)


def pair_product(list_to_multiply):
    distance = len(list_to_multiply) - 1
    pair_list = []
    i = 0
    while distance > 1:
        product = list_to_multiply[i] * list_to_multiply[len(list_to_multiply) - 1 - i]
        pair_list.append(product)
        distance = abs(len(list_to_multiply) - 1 - (2 * i))
        i += 1
    return pair_list


print(list1, '=>', pair_product(list1))
print(list2, '=>', pair_product(list2))

# 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#

print('Задача 3: Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов')

float_list = [1.1, 1.2, 3.1, 5, -10.01]


def decimal_max_dist(float_num_list):
    decimal_list = []
    for item in float_num_list:
        if abs(item) - abs(int(item)) > 0:
            decim = round(abs(item) - abs(int(item)), len(str(item)))
            decimal_list.append(decim)
    dec_length = len(decimal_list)
    max_decimal_diff = 0.0
    for k in range(dec_length):
        for m in range(dec_length):
            if abs(decimal_list[k] - decimal_list[m]) > max_decimal_diff:
                max_decimal_diff = decimal_list[k] - decimal_list[m]
    return max_decimal_diff


print(float_list, '=>', decimal_max_dist(float_list))

#
# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
#


print('Задача 4: Напишите программу, которая будет преобразовывать десятичное число в двоичное')


def to_binary(positive_int: int) -> str:
    bin_string = ''
    while positive_int > 0:
        remainder = positive_int % 2
        bin_string = bin_string + str(remainder)
        positive_int = int(positive_int / 2)
    return bin_string[::-1]


positive = int(input('Введите целое число: '))

print(positive, '=>', to_binary(positive))

#
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов.
#
# *Пример:*
#
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

print('Задача 5: Фибоначчи-список, включая отрицательные')


def fibonacci(n):
    if n < 0 and n % 2 == 0:
        return fibonacci(abs(n)) * -1
    elif n < 0 and n % 2 != 0:
        return fibonacci(abs(n))
    elif n == -1 or n == 1 or n == -2:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def mega_fibonacci_list(n: int) -> list:
    fib_list = [None] * (2 * n + 1)
    for i in range(2 * n + 1):
        num = -n + i
        fib_list[i] = fibonacci(num)
    return fib_list


number = int(input('Введите целое число: '))
print(f'Последовательность Фибоначчи от {-number} до {number}: {mega_fibonacci_list(number)}')
