# Оператор CONTINUE используеться для указания Pathon, что необходимо пропустить всё
# оставшиеся команды в тякущем блоке цикла и продолжить со следующей итерации цикла


while True:
    s = input('Введите что нтбуть: ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало символов')
        continue
    print('Введённая строка достаточной длины: ')    