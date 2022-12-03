
import view
from random import randint
# import controller as con


def add_contact(list):
    list2 = view.get_value()
    if int(len(list)) == 0:
        list2[0] = int(len(list))+1
    else:
        list2[0] = list[int(len(list))-1][0]+1

    list.append(list2)
    return list


def del_contact(list):
    x = view.menu3()
    i = 0
    while x != list[i][0]:
        i += 1
        if i == int(len(list)):
            print('Введен не существующий id')
            break
    else:
        j = input('Введите причину увальнения')
        lst = list[i]
        lst.append(j)
        with open('Del_person.csv', 'a') as f:
            for i in range(int(len(lst))):
                f.write(str(lst[i]) + ";")
            f.write('\n')
        list.pop(i)
    return list


def del_contact2(list):
    x = randint(0, int(len(list))-1)
    j = 'Уволили рандомно'
    lst = list[x]
    lst.append(j)
    with open('Del_person.csv', 'a') as f:
        for i in range(int(len(lst))):
            f.write(str(lst[i]) + ";")
        f.write('\n')

    list.pop(x)
    return list


def to_name_id(list):
    i = 0
    while i < int(len(list)):
        list[i][0] = i+1
        i += 1
    return list


def sort_id(list):
    for i in range(int(len(list))):
        for j in range(int(len(list))):
            if list[i][0] < list[j][0]:
                list[i], list[j] = list[j], list[i]
    return list


def add_imp_contact(list):
    file_name = view.menu4()
    with open(file_name, 'r') as f:
        for line in f:
            list.append(line.split())
        return list


def imp_contact(list):
    file_name = view.menu4()
    with open(file_name, 'r') as f:
        list = []
        for line in f:
            line = line[:-2]
            list.append(line.split(';'))
        return list


def contact():
    file_name = 'Personnel.csv'
    try:
        with open(file_name, 'r+') as f:
            list = []
            for line in f:
                line = line[:-2]
                list.append(line.split(';'))
            return list
    except (FileNotFoundError, PermissionError):
        x = input(
            'Фаила с базой данных персонала нет, хотите создать? 0 - нет 1 - да: ')
        while x != '0' and x != '1':
            x = input(
                'Фаила с базой данных нет, хотите создать? ВЫБЕРЕТЕ ОДИН ИЗ ВАРИАНТОВ 0 - нет 1 - да: ')
        if x == '0':
            exit
        if x == '1':
            with open(file_name, 'w+') as f:
                print('Фаил с базой кадров создан')
            return list


def Del_person():
    file_name = 'Del_person.csv'
    try:
        with open(file_name, 'r+') as f:
            list = []
            for line in f:
                line = line[:-2]
                list.append(line.split(';'))
            return list
    except (FileNotFoundError, PermissionError):
        x = input(
            'Фаила с уволенными кадрами нет, хотите создать? 0 - нет 1 - да: ')
        while x != '0' and x != '1':
            x = input(
                'Фаила с уволенными кадрами нет, хотите создать? ВЫБЕРЕТЕ ОДИН ИЗ ВАРИАНТОВ 0 - нет 1 - да: ')
        if x == '0':
            exit
        if x == '1':
            with open(file_name, 'w+') as f:
                print('Фаил с базой уволенных сотрудников создан')
            return list


def exp_contact2(list, file_name):

    with open(file_name, 'w') as f:
        i = 0
        while i < int(len(list)):
            for j in range(int(len(list[i]))):
                f.write(str(list[i][j]) + ";")
            f.write('\n')
            i += 1


def exp_contact(list):
    file_name = view.menu4()
    with open(file_name, 'w') as f:
        i = 0
        while i < int(len(list)):
            for j in range(int(len(list[i]))):
                f.write(str(list[i][j]) + ";")
            f.write('\n')
            i += 1


def find_all_contact(list):
    x = view.menu5()
    z = not True
    for i in range(int(len(list))):
        for j in range(int(len(list[i]))):
            if list[i][j] == x:
                print(f'Ваш контакт: {list[i]}')
                z = True
                break
            elif i == int(len(list))-1 and j == int(len(list[i]))-1 and z != True:
                print('Поиск нечего не нашел')


def find_surname(list):
    x = view.menu5()
    z = not True
    for i in range(int(len(list))):
        if list[i][2] == x:
            print(f'Ваш контакт: {list[i]}')
            z = True
            break
        elif i == int(len(list))-1 and z != True:
            print('Поиск нечего не нашел')
