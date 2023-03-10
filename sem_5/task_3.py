# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым


num = int(input('Введите число: '))
def IsSimple(num):

    for i in range(2,num):
        if num%i == 0:
            print('Число не простое')
            break
        else:
            if num <=1:
                print('Число ни простое ни составное ')
            else:
                print('Число простое')
IsSimple(num)