# В некоторой школе решили набрать три новых математических класса
# и оборудовать кабинеты для них новыми партами.За каждой партой может 
# сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них. 
# Без циклов и if'ов и без функций
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32


klass_1 = int(input('Введите количество учащихся: '))
klass_2 = int(input('Введите количество учащихся: '))
klass_3 = int(input('Введите количество учащихся: '))
print(f'Нужно {(klass_1+1)//2+(klass_2+1)//2+(klass_3+1)//2} парты')