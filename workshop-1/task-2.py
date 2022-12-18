"""
Задача 2
    Найдите сумму цифр трехзначного числа.
    Пример:
    123 -> 6 (1 + 2 + 3)
    100 -> 1 (1 + 0 + 0)
"""


def sumThreeDigitNumber(num):
    """
    Нахождение суммы цифр трехзначного числа

        Параметры
            num (int): трехзначное число

        Возвращаемое значение
            sumNumber (int): сумма цифр трехзначного числа
    """
    if 100 > num > 999:
        print("Это не трехзначное: ")
    else:
        a = num // 100  # первое число
        b = (num // 10) % 10  # второе число
        c = num % 10   # третье число
        sum_number = a + b + c    # сумма чисел
        print(f'{num} -> {sum_number} ({a} + {b} + {c})')

        return sum_number


number = int(input('Введите трехзначное число: '))

sumThreeDigitNumber(number)
