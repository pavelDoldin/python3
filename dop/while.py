# Игра угадай число 

number = 36         # Загаданное число
running = True      # истина
while running:      # делай
    number_1 = int(input('Угадай число ) '))
    if number_1 == number: 
        print('Поздравляю, вы угадали число !!!')
        running = False   # Останавливает while
    elif number_1 > number:
        print('Ваше число больше загаданного, попробуйте ещё раз.')
    else:
        print('Ваше число меньше загаданного, попробуйте ещё раз. ')