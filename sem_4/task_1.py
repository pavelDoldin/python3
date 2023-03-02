# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n. 
# Решить через словарь!
# приветик
# п_1
# р_1
# и_2
# в_1
# е_1
# т_1
# к_1

stroka = input('Введите слово: ')
d={}
for i in stroka:
    d[i]= d.get (i,0)+1
for k,n in d.items():
    print (f'{k}_{n}')

    # Второе решение 
# for symbol in string:
#     if symbol not in dict:
#         dict[symbol] = 1
#     else:
#         dict[symbol] +=1
# for key, value in dict.items():
#     print(f'{key}_{value}')