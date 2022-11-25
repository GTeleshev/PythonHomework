# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0.56 -> 11

dec_number = float(input('Задача 1. Введите вещественное число: '))


def sum_digits(num_float):
    total_len = len(str(num_float).replace('.', ''))
    int_num = int(num_float)
    int_len = len(str(int_num))
    float_portion = round(num_float - int_num, total_len - int_len + 1)
    norm_int = int((int_num + float_portion) * (10 ** (total_len - int_len)))
    sum_of_digits = 0
    for i in range(total_len):
        sum_of_digits += norm_int % 10
        norm_int = int(norm_int / 10)
    return sum_of_digits


print(f'Сумма цифр числа {dec_number} равна: {sum_digits(dec_number)}')

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# Запрещено использовать функцию factorial из библиотеки math

n2 = int(input('Задача 2 (список - факториалы элементов). Введите N: '))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def generate_factorial_list(N):
    fact_list = [None] * N
    for j in range(N):
        fact_list[j] = factorial(j + 1)
    return fact_list


print('Выходной список: ', generate_factorial_list(n2))


# 3 Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)

def generate_1slash_n(N):
    list_1_slash_N = [None] * N
    for i in range(1, N + 1):
        list_1_slash_N[i - 1] = round((1 + 1 / i) ** i, 2)
    return list_1_slash_N


def sum_of_list_elements(list):
    list_sum = 0
    for m in range(len(list)):
        list_sum = list_sum + list[m]
    return list_sum


n3 = int(input('Задача 3 (список из n чисел последовательности (1 + 1/n)**n, сумма). Введите N: '))
list_n = generate_1slash_n(n3)
print(list_n)
sum_list = sum_of_list_elements(list_n)
print(f'Сумма равна {sum_list}')


# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

def generate_minus_n_to_n(N):
    minus_n_to_n = [None] * (2 * N + 1)
    for k in range(N * 2 + 1):
        minus_n_to_n[k] = -N + k
    print(minus_n_to_n)
    return (minus_n_to_n)


def sum_list_elements(position1, position2, list):
    sum_list_elements = list[position1] + list[position2]
    return sum_list_elements


n = int(input('Задача 4 (список от -N, N. Суммирование элементов). Введите N: '))

if n < 0:
    n = -n

pos1 = int(input('Введите позицию первого элемента: '))
pos2 = int(input('Введите позицию первого элемента: '))

list_2n = generate_minus_n_to_n(n)

if pos1 > n or pos2 > n:
    print('Позиции элементов не могут быть больше N')
else:
    sum_pos1_pos2 = sum_list_elements(pos1, pos2, list_2n)
    print(f'Сумма элемента №{pos1}({list_2n[pos1]}) и элемента №{pos2}({list_2n[pos2]}) равна {sum_pos1_pos2}')

# 5 Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

import random

print('Задача 5 (перемешивание списка)')
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def mix_list(input_list):
    len_list = len(input_list)
    new_list = [None] * len_list
    for i in range(len_list):
        k = random.randint(0, len_list - 1)
        new_list[k] = input_list[i]
        new_list[i] = input_list[k]
    return new_list

def list_overlap(list1, list2):
    overlap = float(0.0)
    count = 0
    if len(list1) != len(list2):
        raise Exception('Длина списков различна')
    else:
        for j in range(len(list1)):
            if list1[j] == list2[j]:
                count += 1
    overlap = 100 * (count / len(list1))
    return overlap

list_2 = mix_list(list_1)

print('Исходный список:\n', list_1)
print('Перемешанный список:\n', list_2)
print('Пересечение списков, %: ', list_overlap(list_1, list_2))

