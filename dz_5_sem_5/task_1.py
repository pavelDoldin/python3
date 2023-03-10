# Напишите программу, которая на вход принимает два числа A и B, и возводит 
# число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def degree(a,b):
    if b == 0:
        return 1
    if b<0:
        return 1/degree(a, -b)
    if b%2 == 0:
        return degree(a,b//2) * degree(a,b//2)
    else:
        return degree(a, b-1) * a

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

print(f'Степень ровна {degree(a,b)}')