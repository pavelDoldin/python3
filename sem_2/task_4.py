# Введите количество арбузов N, 
# Найдите максимальное и минимальное вес арбузов.


n = int(input('Введите количество арбузов: '))
max = 0
min = 10000000
for i in range(n):
    ves_arbyz = int(input('Введите вес арбуза: '))
    if ves_arbyz < min:
        min = ves_arbyz
    if ves_arbyz > max:
        max = ves_arbyz
print(f'Максимальный вес {max}, и мимальный вес {min}')