# Дан массив, состоящих из целых чисел. Напишите программу, которая в данном массиве
# определяет количество элементов, у которых два соседних, и при этом, оба соседних
# элементов меньше данного. Сначала dводится число N - количество элементов в массиве
# далее записаны N чисел - элемента массива. Массив состоит из целых чисел.


# import func
# array = func.FillArray()
count = 0
array_n = []
n = int(input('Введите количество элементов: '))
for j in range(n):
    a = int(input('Введите элементы: '))
    array_n.append(a)
for i in range(1,(len(array_n)-1)):
    if array_n[i-1] < array_n[i] > array_n[i+1]:
        count += 1
print(*array_n)
print(count)
