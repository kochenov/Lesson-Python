"""
    Задача 12
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.

"""

from math import sqrt


# P = a*b       a = P/b    P/b = S-b      p = Sb -  bb   b^2-Sb+P=0  D = s^2-4P
# S = a+b       a = S-b
def calculate(sum_numbers, multiplication):
    disclaimer = sum_numbers * sum_numbers - 4 * multiplication  # считаем дискриминант
    if disclaimer > 0:  # если дискриминант > 0 - два корня
        x = sum_numbers / 2 - sqrt(disclaimer) / 2
        y = sum_numbers / 2 + sqrt(disclaimer) / 2
    return [x, y]


def main():
    b = int(input('Введите сумму: '))
    c = int(input('Введите произведение: '))
    print(calculate(b, c))


main()
