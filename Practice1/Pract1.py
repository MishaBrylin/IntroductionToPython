# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
day = int(input('Введите день недели от 1 до 7: '))
if day == 6 or day == 7:
    print('Этот день недели выходной')
else:
    print('Этот день недели не выходной')

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in [1, 0]:
    for y in [1, 0]:
        for z in [1, 0]:
            print(f'Не ({x} или {y} или {z}) = не {x} и не {y} и не {z}')
            print((not (x or y or z)) == (not x) and (not y) and (not z))


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x, y = int(input('Введите кординату X: ')), int(input('Введите кординату Y: '))
if (x > 0 and y > 0):
    print('Точка находится в 1 четверти')
if (x < 0 and y > 0):
    print('Точка находится в 2 четверти')
if (x < 0 and y < 0):
    print('Точка находится в 3 четверти')
if (x > 0 and y < 0):
    print('Точка находится в 4 четверти')
if (x == 0 and y != 0):
    print('Точка находится на оси x')
if (y == 0 and x != 0):
    print('Точка находится на оси y')
if (x == 0 and y == 0):
    print('Точка находится в середине оси x и y')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
quarter_number = int(input('Введите номер четверти: '))
if (quarter_number == 1):
    print('Диапазон кординат x > 0 и y > 0')
if (quarter_number == 2):
    print('Диапазон кординат x < 0 и y > 0')
if (quarter_number == 3):
    print('Диапазон кординат x < 0 и y < 0')
if (quarter_number == 4):
    print('Диапазон кординат x > 0 и y < 0')

    
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
x1, y1 = float(input('Введите кординату X1: ')), float(
    input('Введите кординату Y1: '))
x2, y2 = float(input('Введите кординату X2: ')), float(
    input('Введите кординату Y2: '))
print(
    f'Растояние между двумя точками = {float((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))**(0.5)}')
