# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить 
# в нем только двузначные числа.Реализовать программу с использованием 
# функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]


list_1 = [int(x) for x in input('Введите числа: ').split()]
res = list(filter(lambda x: abs(x) > 9 and abs(x) < 100, list_1))
print(res)