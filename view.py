

from prettytable import PrettyTable
import model as m


def menu():
    print('''Для работы с базой по кадрам необходимо выбрать один из вариантов:
    Посмотреть весь персонал: - 1
    Уволить случайного сотрудника: - 2
    Добавление записи: - 3
    Удаление сотрудника (уволить) id: - 4
    Создать новый базу персонала, импортировав ее из файла: - 5
    Добавить базу в уже имеющую базу из файла: - 6
    Экспортировать базу в файл: - 7 
    Присвоить новые id по порядку: - 8
    Сортировать по порядку по id: - 9
    Найти в базе (поиск происходит по любой записи) - 10
    Найти в базе по фамилии - 11
    Показать список уволенных сотрудников - 12
    Выйти из базы - 13''')

    n = int(input('Введите номер: '))
    while not 0 < n < 14:
        n = int(input('Введите номер из меню от 1 до 13: '))
    return n


def menu2():
    n = int(input('Чтобы вернуться в меню нажмите 0 '))
    while not n == 0:
        n = int(input('Введите 0: '))


def menu3():
    x = input('Введите номер id справочника, чтбы удалить запись: ')

    return x


def menu4():
    x = input('Укажите название фаила: ')

    return x


def menu5():
    x = input('Укажите цель поиска: ')
    return x


def get_value():
    lst = [1, ]
    x = input('Введите имя: ')
    lst.append(x)
    x = input('Введите фамилию: ')
    lst.append(x)
    x = input('Введите день рождения: ')
    lst.append(x)
    x = input('Введите место работы: ')
    lst.append(x),
    x = input('Введите номер телефона: ')
    lst.append(x)
    return lst


def show_contact():
    list = m.Del_person()
    i = 0
    new_Table = PrettyTable(
        ["id", "имя", "фамилия", "день рождения", "должность", "номер телефона", "Причина увольнения"])

    while i < int(len(list)):
        new_Table.add_row([list[i][0], list[i][1], list[i][2],
                           list[i][3], list[i][4], list[i][5], list[i][6]])
        i += 1
    print(new_Table)


def show_contact2(list):
    i = 0
    new_Table = PrettyTable(
        ["id", "имя", "фамилия", "день рождения", "место работы", "номер телефона"])

    while i < int(len(list)):
        new_Table.add_row([list[i][0], list[i][1], list[i][2],
                           list[i][3], list[i][4], list[i][5]])
        i += 1
    print(new_Table)
