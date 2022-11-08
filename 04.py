# 4) Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

import random

k = input('Введиите степень многочлена: ')
f = f'{random.randint(0, 100)} = 0'
for i in range(int(k)):
    z = random.randint(0, 100)

    if i == 0:
        f = f'{z}x + {f} '
    elif z == 0:
        f = {z} + f
    else:
        f = f'{z}x^{i+1} + {f}'
if len(f) > 6:
    data = open('file.txt', 'a')
    data.writelines(f'{f}\n')
    data.close()
else:
    print('Порпрубуйте еще раз')