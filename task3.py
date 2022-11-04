# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.2
import random
x = int(input('введите длину списка: '))
list = []

for i in range(0, x, 1):
    list.append(round(random.randint(10, 100) +
                (random.randint(0, 10)/10)*(random.randint(10, 100)/100), 2))


print(list)

min = 1
max = 0
for i in list:
    if (i - int(i)) <= min:
        min = i - int(i)

    if (i - int(i)) >= max:
        max = i - int(i)

print(round(max-min, 2))
