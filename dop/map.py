# Произвести list строк в list чисел.


data = '1 4 6 8 54 3 25 89 70'
print(data)
data = list(map(int, data.split()))
print(data)