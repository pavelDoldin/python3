# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи,
# выведите число -1.


# n = int(input('Введите число: '))
# f_1 = 1
# f_2 = 1
# num_index = 2
# while f_2 < n:
#     num_index += 1
#     f_1, f_2 = f_2, f_1 + f_2

# if f_2 == n:
#     print(num_index)
# else:
#     print(-1)

# n = int(input())

n = int(input('Введите число: '))
prev_num = 0
current_num = 1
temp = None
count = 0
while current_num <= n:
    temp = prev_num
    prev_num = current_num + prev_num
    current_num = temp
    count += 1
    if n == current_num:
        print(count)
        break
else:
    print ("Число не является числом Фибонначи")