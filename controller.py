import view as v
import model as m
import logger as l

lst = m.contact()



def run():
    x = lst

    z = True
    while z:
        n = v.menu()

        if n == 1:
            v.show_contact2(x)
            l.logger('Просмотр контактов')
            v.menu2()
        elif n == 2:
            x = m.del_contact2(x)
            m.exp_contact2(x, 'Personnel.csv')
            l.logger('Удаление случайного сотрудника')
            v.menu2()
        elif n == 3:
            x = m.add_contact(x)
            m.exp_contact2(x, 'Personnel.csv')
            l.logger('Добавление контакта')
            v.menu2()

        elif n == 4:
            x = m.del_contact(x)
            m.exp_contact2(x, 'Personnel.csv')
            l.logger('Удаление контакта')
            v.menu2()

        elif n == 5:
            x = m.imp_contact(x)
            m.exp_contact2(x, 'Personnel.csv')
            l.logger('Импорт контактов')
            v.menu2()

        elif n == 6:
            x = m.add_imp_contact(x)
            m.exp_contact2(x, 'Personnel.csv')
            l.logger('Добавление имортированных контактов')
            v.menu2()

        elif n == 7:
            m.exp_contact(x)
            l.logger('Экспорт контактов')
            v.menu2()
        elif n == 8:
            x = m.to_name_id(x)
            m.exp_contact2(x, 'Personnel.csv')
            l.logger('Присвоены новые id попорядку')
            v.menu2()
        elif n == 9:
            x = m.sort_id(x)
            m.exp_contact2(x, 'Personnel.csv')
            l.logger('Сортировка id попорядку')
            v.menu2()

        elif n == 10:
            m.find_all_contact(x)
            l.logger('Поиск контакта')
            v.menu2()

        elif n == 11:
            m.find_surname(x)
            l.logger('Поиск контакта по фамилии')
            v.menu2()

        elif n == 12:
            v.show_contact()
            l.logger('Показывает список уволенных сотрудников')
            v.menu2()

        elif n == 13:
            z = False
