# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

weekday_number = int(input('Введите номер дня недели (1-7): '))

if weekday_number == 6 or weekday_number == 7:
    print('да')
elif weekday_number < 1 or weekday_number > 7:
    print('число не находится в диапазоне от 1 до 7')
else:
    print('нет')

print('-------------------')
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

check = -100

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            if (not(X or Y or Z)) == ((not X) and (not Y) and (not Z)):
                check = True
                print(f'X = {bool(X)}, Y = {bool(Y)}, Z = {bool(Z)}. Statement is: {check}')
            else:
                check = False
                break

print(f'Statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is: {check} in all possible permutations of X,Y,Z')

print('-------------------')

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input('x = '))
y = float(input('y = '))

if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x == 0 and y == 0:
    print('Точка лежит в начале координат')
elif x == 0:
    print('Точка лежит на оси X')
elif y == 0:
    print('Точка лежит на оси Y')
else:
    print('Четвертая четверть')

print('-------------------')
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quadrant_number = int(input('Введите номер четверти (1-4): '))

if quadrant_number == 1:
    print('x = (0, +oo), y = (0, +oo)')
elif quadrant_number == 2:
    print('x = (0, -oo), y = (0, +oo)')
elif quadrant_number == 3:
    print('x = (0, -oo), y = (0, -oo)')
elif quadrant_number == 4:
    print('x = (0, +oo), y = (0, -oo)')
else:
    print('Введите число от 1 до 4')

print('-------------------')
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

A = input('Точка A (x1,y1):').split(',')
B = input('Точка B (x2,y2):').split(',')

distance = round(((float(A[0]) - float(B[0])) ** 2 + (float(A[1]) - float(B[1])) ** 2) ** 0.5, 3)
print(f'Расстояние между точками равно: {distance}')