# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)



n = int(input('Введите количество элементов массива: '))
array_n = [int(input('Введите элементы: ')) for i in range(n)]
min = int(input('Введите минимум: '))
max = int(input('Введите максимум: '))
print(array_n)
print(min, max)
for j in range(len(array_n)):
    if min <= array_n[j] and array_n[j]<= max:
        print(j)