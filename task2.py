# 1 – Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
x = list(input('Введите число: '))
sum = 0
for i in range(len(x)):
    if x[i] != '.' and ',' :
        sum = sum+int(x[i])
    else:
        continue
print(sum)
# 2 –Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
x = int(input('Введите число: '))
y = 1
for i in range(x):
    y=(i+1)*y
    print(y,  end=' ')
print()

# 3 – Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037
n = int(input('Введите число: '))
y = {}
sum = 0
for i in range(n):
    y[i] = (1 + 1/(i+1))**(i+1)
    sum = y[i] + sum
print(sum)


# 4 – Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

N = int(input('Введите число: '))
lst1 = {}
for i in range(N):
    lst1[i] = random.randint(-N, N)
print(lst1)
mult = 1
data = open('file.txt', 'r')
for line in data:
    if int(line.rstrip('\n')) <= N-1:
        mult = mult * lst1[(int(line.rstrip('\n')))]
    else:
        print('Что-то не то')
    
print(mult)   
data.close()


# 5 – Реализуйте алгоритм перемешивания списка.
N = int(input('Введите число: '))
lst1 = {}
for i in range(N):
    lst1[i] = i+1
print(lst1)

for i in range(N):
    z = random.randint(0, N-1)
    x = lst1[i]
    lst1[i] = lst1[z]
    lst1[z] = x
print(lst1)
