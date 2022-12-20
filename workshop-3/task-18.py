"""
    Задача 18:

Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N/2.
Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший.

    Пример:
        Ввод: 5
        Ввод: 6
        1 2 0 4 7
        Вывод: 7
"""

import random

n = int(input("Введите число N: "))
x = int(input("Введите число X: "))

list_num = []

for num in range(n):
    random_number = round(random.randint(1, (n // 2)))
    list_num.append(random_number)

number = 0

for i in range(len(list_num)):
    if (x - list_num[i]) < x - number and x - list_num[i] > 0:
        number = i
print(list_num)
print(list_num[number])
