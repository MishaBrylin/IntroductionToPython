

from prettytable import PrettyTable


def menu():
    print('''Для работы с телефонным справочником введите число:
    Просмотр всех записей справочника: - 1
    Просмотр всех записей справочника(красивой таблицей): - 2
    Добавление новой записи: - 3
    Удаление записи из справочника по id: - 4
    Создать новый справочник импортировав справочник из фаила: - 5
    Добавить контакты в уже имеющий справочник из файла: - 6
    Экспортировать справочник в файл: - 7 
    Присвоить новые id попорядку: - 8
    Сортировать попорядку по id: - 9
    Найти в справочнике (поиск происходит по любой записи) - 10
    Найти в справочнике по фамилии - 11
    Выйти из справочника - 12''')
    n = int(input('Введите номер: '))
    while not 0 < n < 13:
        n = int(input('Введите номер из меню от 1 до 12: '))
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


def show_contact(list):
    i = 0
    while i < int(len(list)):
        for j in range(int(len(list[i]))):
            print(list[i][j], end=' ')
        i += 1
        print()
        print()


def show_contact2(list):
    i = 0
    new_Table = PrettyTable(
        ["id", "имя", "фамилия", "день рождения", "место работы", "номер телефона"])

    while i < int(len(list)):
        new_Table.add_row([list[i][0], list[i][1], list[i][2],
                           list[i][3], list[i][4], list[i][5], ])
        i += 1
    print(new_Table)
