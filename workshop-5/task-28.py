# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def suma(a, b):
    if b == 0:
        return a
    else:
        return a + suma(1, b - 1)


def numberA():
    a = int(input('Введите первое число: '))
    if a < 0:
        print('Некорректный ввод! Введите целые неотрицательные числа. ')
        return numberA()
    else:
        return a


def numberB():
    b = int(input('Введите второе число: '))
    if b < 0:
        print('Некорректный ввод! Введите целые неотрицательные числа. ')
        return numberB()
    else:
        return b


A = numberA()
B = numberB()
result = suma(A, B)
print(f'{A} + {B} = {result}')
