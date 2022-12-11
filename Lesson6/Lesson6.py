# Урок 3, Задача 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# *Пример:*
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print('Урок 3, Задача 1. Сумма элементов списка, стоящих на нечётной позиции')

num_list = [2, 3, 5, 9, 3, -11]
print('Список: ', num_list)

# Старый код
def odd_sum(numlist):
    sum = 0
    for i in range(1, len(numlist), 2):
        sum += numlist[i]
    return sum

print("Сумма (код без функций): ", odd_sum(num_list))

# Код с list comprehension + enumerate
sum_odd = sum([y for x, y in enumerate(num_list) if x % 2 != 0])
print("Сумма (list comprehension + enumerate): ",sum_odd)
print('\n')
# Урок 3, Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#

print('Урок 3, Задача 3: Напишите программу, которая найдёт разницу между\n максимальным и минимальным значением дробной части элементов')

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


print('Старый код: ', float_list, '=>', decimal_max_dist(float_list))

# новый код (map, list comprehension)
dec_list = list(map(lambda x: round(abs(x) - abs(int(x)), len(str(x))), float_list))
non_zero_list = [x for x in dec_list if x > 0]
print('Map, вычисление дробной части: ', dec_list)
print('List comprehension -> ненулевые элементы: ', non_zero_list)
print('Максимум - минимум: ', max(non_zero_list) - min(non_zero_list))
print('\n')
# Урок 4, Задача 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
# [1, 1, 1, 2, 2, 3, 5, 4, 4, 7, 8, 8, 7] -> [3, 5]

print('Урок 4, Задача 3. Вывод список неповторяющихся элементов последовательности')

list_1 = [1, 1, 1, 2, 2, 3, 5, 4, 4, 7, 8, 8, 7, 13, 11, 10, 78]

# Старый код
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


print('Исходный лист: ', list_1)
print('Старый код: ', unique_elements(list_1))

# Код с List comprehension

unique = [x for x in list_1 if list_1.count(x) < 2]
print('Код с List comprehension: ', unique)
# Код с List filter
unique1 = list(filter(lambda x: list_1.count(x) < 2, list_1))
print('Код с filter(): ', unique1)
print('\n')
# Урок 5, Задача 1. Напишите программу, удаляющую из файла все слова, содержащие "абв".
# (исходный код реализован с использованием filter())
print('Урок 5, Задача 1. Напишите программу, удаляющую из файла все слова, содержащие "абв" \n (исходный код реализован с использованием filter())')

with open('abv.txt', 'r') as file:
    string_text = file.readline()

substring = 'абв'

print('Исходная строка: ', string_text)
print('Текст к удалению: ', substring)

text_lst = string_text.split(" ")
output_lst = list(filter(lambda x: x.lower().find(substring) == -1, text_lst)) # filter()
output_txt = " ".join(output_lst)
print("Будет записан текст: ", output_txt)

with open('withoutabv.txt', 'w') as file:
    file.write(output_txt)

