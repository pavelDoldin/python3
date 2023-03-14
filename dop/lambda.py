# В списке храняться числа, нужно выбрать только чётные числа и составить 
# список пар (число, кводрат числа)
# пример: 1 2 3 5 8 15 23 38
# вывод [(2, 4), (8, 64), (38, 1444)]

            # Первое решение 
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)

            # Второе решение

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)