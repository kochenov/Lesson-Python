# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
#
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
#
# Output: 11 6
# 6 12


import random as r

n = int(input('Введите число n, количество элементов первого набора:'))
m = int(input('Введите число m, количество элементов второго набора:'))

l1 = []
for i in range(0, n):
    l1.append(r.randint(0, 2 * (n + m)))
l2 = []
for i in range(0, m):
    l2.append(r.randint(0, 2 * (n + m)))
print(l1, '\n', l2)

res = []
l1 = set(l1)
for item in l1:
    if item in l2:
        res.append(item)
if len(res) != 0:
    print('Результат:', res)
else:
    print('Нет результата')