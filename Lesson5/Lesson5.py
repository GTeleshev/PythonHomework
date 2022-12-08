# 1. Напишите программу, удаляющую из файла все слова, содержащие "абв".
#
print('Задача 1. Напишите программу, удаляющую из файла все слова, содержащие "абв"')

with open('abv.txt', 'r') as file:
    string_text = file.readline()

substring = 'абв'

print('Исходная строка: ', string_text)
print('Текст к удалению: ', substring)

text_lst = string_text.split(" ")
output_lst = list(filter(lambda x: x.lower().find(substring) == -1, text_lst))
output_txt = " ".join(output_lst)
print("Будет записан текст: ", output_txt)

with open('withoutabv.txt', 'w') as file:
    file.write(output_txt)

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.  Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

print('Задача 2. Программа для игры с конфетами')

from random import randint

jackpot = 2021
max_step = 28
remainder = jackpot


def user_input(step):
    inp = False
    bet = 0
    while inp == False or bet not in range(1, step + 1):
        bet_str = input(f'Введите число от 1 до {step}: ')
        inp = bet_str.isdigit()
        if inp: bet = int(bet_str)
    return bet


def bot(rem):
    if rem > max_step * 2:
        return max_step
    elif 28 < rem <= max_step:
        return 1
    elif rem <= 28:
        return rem
    else:
        return 1


def rotate_gen_user(user: int, mode):
    if mode == 1:
        if user == 1:
            return 2
        elif user == 2:
            return 1
    if mode == 2: return randint(1, 2)


def check_score(remainder, bet):
    if remainder - bet < 0:
        return -100
    elif remainder - bet == 0:
        return 0
    elif remainder - bet > 0:
        return 100


def candy_game(remainder):
    players = {1: "Игрок 1",
               2: "Игрок 2"}
    game_step = 1
    inp = False
    mode = 1
    bet = 0
    while inp == False or mode > 2 or mode < 1:
        mode_str = input(f'Выберите режим игры (1 - PvP, 2 - игра с ботом): ')
        inp = mode_str.isdigit()
        if inp: mode = int(mode_str)
    c_user = rotate_gen_user(1, 2)
    print(f"Первым начинает: {players[c_user]}")
    while check_score(remainder, bet) != 0:
        print(f"Ход {game_step}, {players[c_user]}, остаток: {remainder}")
        if mode == 1:
            bet = user_input(max_step)
        elif mode == 2 and c_user == 1:
            bet = user_input(max_step)
        elif mode == 2 and c_user == 2:
            bet = bot(remainder)
            print(f'Бот забирает {bet} конфет')
        ##
        if check_score(remainder, bet) == 100:
            remainder = remainder - bet
        elif check_score(remainder, bet) == -100:
            print('Нельзя забрать больше остатка, установлено: 1')
            remainder = remainder
        elif check_score(remainder, bet) == 0:
            print(f'Выиграл {players[c_user]}')
        c_user = rotate_gen_user(c_user, 1)
        game_step += 1


candy_game(remainder)

# 3. Создайте программу для игры в "Крестики-нолики".
# print('Задача 3. Крестики-нолики')
#
print('Задача 3. Крестики-нолики')
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
position_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_matrix(d2_list):
    for i in range(len(d2_list)):
        for j in range(len(d2_list[i])):
            print(d2_list[i][j], end=" ")
        print()
    print("_____")


def print_positions(d2_list: list):
    for i in range(len(d2_list)):
        for j in range(len(d2_list[i])):
            x = d2_list[i][j]
            if x == -1:
                print('x', end=" ")
            elif x == 1:
                print('o', end=" ")
            else:
                print("-", end=" ")
        print(" ")
    print("_____")


def check_score(pos_matrix: list):
    a = [0] * 8
    a[0] = pos_matrix[0][0] + pos_matrix[1][1] + pos_matrix[2][2]  # первая диагональ
    a[1] = pos_matrix[0][2] + pos_matrix[1][1] + pos_matrix[2][0]  # вторая диагональ
    a[2] = pos_matrix[0][0] + pos_matrix[1][0] + pos_matrix[2][0]  # столбец 1
    a[3] = pos_matrix[0][1] + pos_matrix[1][1] + pos_matrix[2][1]  # столбец 2
    a[4] = pos_matrix[0][2] + pos_matrix[1][2] + pos_matrix[2][2]  # столбец 3
    a[5] = pos_matrix[0][0] + pos_matrix[0][1] + pos_matrix[0][2]  # строка 1
    a[6] = pos_matrix[1][0] + pos_matrix[1][1] + pos_matrix[1][2]  # строка 2
    a[7] = pos_matrix[2][0] + pos_matrix[2][1] + pos_matrix[2][2]  # строка 3
    min_sc = min(*a)
    max_sc = max(*a)
    if min_sc == -3 and max_sc != 3:
        return -3
    elif max_sc == 3 and min_sc != -3:
        return 3
    elif max_sc == 3 and min_sc == -3:
        return 100
    else:
        return 0


def place_xo(board: list, player):
    pos = int(input('Введите позицию: '))
    row = 0
    column = 0
    for i in range(len(position_numbers)):
        for j in range(len(position_numbers)):
            if position_numbers[i][j] == pos:
                row = i
                column = j
    if board[row][column] != 0:
        return False
    else:
        board[row][column] = player
        return True


def rotate_player(player):
    if player == -1: return 1
    if player == 1: return -1


def game(board: list, player=-1):
    count = 1
    print("Номера клеток: ")
    print_matrix(position_numbers)
    while check_score(board) == 0 and count <= 9:
        print('Игрок: ', player)
        print('Ход: ', count)
        place_xo(board, player)
        score = check_score(board)
        player = rotate_player(player)
        print_positions(board)
        count += 1
    if score == -3:
        print("Игрок 1 выиграл")
    elif score == 3:
        print("Игрок 2 выиграл")
    elif score == 100 or count > 9:
        print("Ничья")


game(board)

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff

print('Задача 4. RLE алгоритм')

with open('RLE_input.txt', 'r') as file:
    string_text = file.readline()

print('Исходная строка: ', string_text)


def pack_string(inp_str: str):
    length = len(inp_str)
    dict_unique = {}
    count = 1
    for i in range(1, length):
        if inp_str[i] == inp_str[i - 1]:
            count = count + 1
            dict_unique[inp_str[i - 1]] = count
        elif inp_str[i] != inp_str[i - 1]:
            count = 1
            dict_unique[inp_str[i]] = count
    return dict_unique


def print_dict_rec(inp_dict: dict):
    output_string = ""
    keys = inp_dict.keys()
    for l in keys:
        output_string += l * inp_dict[l]
    return output_string


def print_dict_sing(inp_dict: dict):
    output_string = ""
    keys = inp_dict.keys()
    for l in keys:
        output_string += str(inp_dict[l]) + l
    return output_string


print('"Упакованная" строка для записи в выходной файл: ', print_dict_sing(pack_string(string_text)))

with open('RLE_output.txt', 'w') as file:
    file.writelines(print_dict_sing(pack_string(string_text)))

print('"Распакованная" строка для повторной записи во входной файл', print_dict_rec(pack_string(string_text)))

with open('RLE_input.txt', 'w') as file:
    input_string = file.writelines(print_dict_rec(pack_string(string_text)))

# 5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

print('Задача 5. Дан список чисел. Найдите все возрастающие последовательности')

list_num1 = [1, 5, 2, 3, 4, 6, 1, 7]
list_num2 = [7, 5, 2, 3, 4, 6, 1, 7]


def is_list_ordered(list_num: list):
    for k in range(1, len(list_num)):
        if list_num[k - 1] > list_num[k]:
            return False
    return True


# генерация всех несмежных подпоследовательностей https://rosettacode.org/wiki/Non-continuous_subsequences#Python
def non_consectuive_substrings(seq, s=0):
    if seq:
        x = seq[:1]
        xs = seq[1:]
        p2 = s % 2
        p1 = not p2
        return [x + ys for ys in non_consectuive_substrings(xs, s + p1)] + non_consectuive_substrings(xs, s + p2)
    else:
        return [[]] if s >= 3 else []


def ordered_sub_lists(test_str: list):
    out = []
    res = [test_str[i: j] for i in range(len(test_str))
           for j in range(i + 2, len(test_str) + 1)]
    for l in res:
        if is_list_ordered(l):
            out.append(l)
    for j in non_consectuive_substrings(test_str):
        if is_list_ordered(j):
            out.append(j)
    return out


print('Исходный список 1: ', list_num1)
print(
    f'Число возрастающих подпоследовательностей: {len(ordered_sub_lists(list_num1))}. Список: {ordered_sub_lists(list_num1)}')

print('Исходный список 2: ', list_num2)
print(
    f'Число возрастающих подпоследовательностей: {len(ordered_sub_lists(list_num2))}. Список: {ordered_sub_lists(list_num2)}')