from prettytable import PrettyTable
 
d = {'11': ' ', '12': ' ', '13': ' ', '21': ' ', '22': ' ', '23': ' ', '31': ' ', '32': ' ', '33': ' '}
 
 
def finish(f, k):
    print(f'Победили {f}')
    print(k)
 
 
for i in range(9):
 
    x = input('Введите координаты, без пробела два числа. Первое число координаты x второе число координаты y (например 12 или 33 или 11). Сначала X потом У: ')
    while not x in d:
        x = input('Введите правельные координаты: ')
    while d[x] == '0' or d[x] == 'X':
        x = input(f'Введены координаты, где уже есть {d[x]}: ')
    if i % 2 == 0:
        d[x] = 'X'
    else:
        d[x] = '0'
 
    table = PrettyTable(['Коррдинаты', 'x = 1', 'x = 2', 'x = 3'])
    table.add_row(['y = 1', d['11'], d['12'], d['13']])
    table.add_row(['y = 2', d['21'], d['22'], d['23']])
    table.add_row(['y = 3', d['31'], d['32'], d['33']])
    if d['11'] == d['12'] == d['13'] != ' ':
        finish(d[x], table)
        break
    if d['21'] == d['22'] == d['23'] != ' ':
        finish(d[x], table)
        break
    if d['31'] == d['32'] == d['33'] != ' ':
        finish(d[x], table)
        break
    if d['11'] == d['21'] == d['31'] != ' ':
        finish(d[x], table)
        break
    if d['12'] == d['22'] == d['32'] != ' ':
        finish(d[x], table)
        break
    if d['13'] == d['23'] == d['33'] != ' ':
        finish(d[x], table)
        break
    if d['11'] == d['22'] == d['33'] != ' ':
        finish(d[x], table)
        break
    if d['31'] == d['22'] == d['13'] != ' ':
        finish(d[x], table)
        break
    print(table)
