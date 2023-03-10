# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются только
#  +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 


def rec_sum(a,b):
    if b == 0:
        return a
    elif b > 0:
        return rec_sum(a + 1, b - 1)
    return rec_sum(a - 1, b + 1)

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
print(f'Cумма ровна: {rec_sum(a, b)}')
