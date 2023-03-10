# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
#
# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )
#
# Output: 9

import random as r

n = int(input('Количество кустов: '))
l1 = []
for i in range(0, n):
    l1.append(r.randint(1, 2 * n))
print('Черники: ', l1)
res = 0
for i in range(len(l1) - 1):
    if (l1[i - 1] + l1[i] + l1[i + 1]) > res:
        res = l1[i - 1] + l1[i] + l1[i + 1]
print('Максимальное число ягод: ', res)
