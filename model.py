import view
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
        list.pop(i)
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
 
 
def exp_contact(list):
    file_name = view.menu4()
    with open(file_name, 'w') as f:
        i = 0
        while i < int(len(list)):
            for j in range(int(len(list[i]))):
                f.write(str(list[i][j]) + ";")
            f.write('\n')
            i += 1
    return list
 
 
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
