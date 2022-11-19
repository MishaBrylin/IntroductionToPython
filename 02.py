# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

list1 = [1, 2, 3, 5, 1, 5, 3, 10]

list2 = []
list3 = []
list4 = []
for i in list1:
    if list1.count(i) < 2:
        list2.append(i)

for i in list1:
    if list1.count(i) >= 2:
        if i not in list3:
            list3.append(i)

for i in list1:
    if i not in list4:
            list4.append(i)

print(list2)
print(list3)
print(list4)