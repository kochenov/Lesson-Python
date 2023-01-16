# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def degree(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * degree(a, b - 1)
    else:
        return 1 / a * degree(1 / a, abs(b) - 1)


A = int(input('Введите число: '))
B = int(input('Введите степень числа: '))
print(f'{A} в степени {B} = {degree(A, B)}')
