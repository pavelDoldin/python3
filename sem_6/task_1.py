# Даны два массива чисел. Требуеться вывести те элементы первого массива, (в том порядке
# в котором онни идут в первом массиве). Которых нет во втором массиве. Пользователь 
# вводит N - количество элементов в первом массиве, затем N чисел элементы мвссива.
# затем число M - количество элементов во втором массиве. Затем элементы второго массива.

            # Моё решение, наверно не правельно. В задаче через массив надо решить.

# one_n = int(input('Введите количество элементов N: '))
# n_array = {int(input('Введите элементы N: ')) for i in range(one_n)}
# two_m = int(input('Введите количество элементов M: '))
# m_array = {int(input('Введите элементы M: '))for j in range(two_m)}
# s = n_array.difference(m_array)

# print(f'Первый массив: {n_array}')
# print(f'Второй массив: {m_array}')
# print(*s)


            # Решение группы переделал, работает !!!
array_n = []
array_m = []
n = int(input('Введите количечтво элементов N: '))
for i in range(n):
    a = int(input('Введите элементы N: '))
    array_n.append(a)

m = int(input('Введите количество элементов M: '))
for i in range(m):
    b = int(input('Введите элементы M: '))
    array_m.append(b)

print(*array_n)
print(*array_m)

for i in array_n:
    if i not in array_m:
        print(i, end= ' ')

# for i in array_n:
#     for j in array_m:
#         if i == j:
#             break
#     else:
#         print(i, end= ' ')