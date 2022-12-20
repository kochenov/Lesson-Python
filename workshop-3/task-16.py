"""
    Задача 16:
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь вводит натуральное число N – количество элементов в массиве.
и число, которое необходимо проверить - X.

Заполните массив случайными натуральными числами от 1 до N/2.
Выведите, сколько раз X встречается в массиве.

    Пример:
        Ввод: 5
        Ввод: 3

        1 2 3 4 5
        Вывод: 1
"""

import random

n = int(input("Введите число N: "))
x = int(input("Введите число X: "))

list_num = []

for num in range(n):
    random_number = round(random.randint(1, (n // 2)))
    list_num.append(random_number)

print(list_num)

count = 0

for i in range(len(list_num)):
    if list_num[i] == x:
        count += 1
print("Линейный поиск: ", count)


print("Используя особенность языка: ", list_num.count(x))
