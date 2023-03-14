# Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

            # Первое решение 
num = input('Введите число: ')
res = list(filter(lambda x: x != ',' and x != '.' and x != '-', num))
res = sum(list(map(lambda x: int(x), res)))
print(res)

            # Второе решение
# print(sum(map(int, filter(lambda el: el.isdigit(), input('Enter a number: ')))))