# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет 
# определенную ценность. В случае с английским алфавитом очки распределяются 
# так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу,
# которая вычисляет стоимость введенного пользователем слова. Будем считать, 
# что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.
# ноутбук
# 12

            # Чесно списал с 21 строчки (
slovar_en = {1 : 'AEIOULNSTR', 2 : 'DG', 3 : 'BCMP', 4 : 'FHVWY', 5 : 'K',
             8 : 'JX', 10 : 'Q Z'}
slovar_ru = {1 : 'АВЕИНОРСТ', 2 : 'ДКЛМПУ', 3 : 'БГЁЬЯ', 4 : 'ЙЫ', 
             5 : 'ЖЗХЦЧ', 8 : 'ШЭЮ', 10 : 'ФЩЪ',}
count = 0
slovo = input('Введите слово: ').upper()
for i in slovo:
    if i in  'AEIOULNSTRDGBCMPFHVWYKJXQZ':
        for j in slovar_en:
            if i in slovar_en[j]:
                count = count + j
    else:
        for j in slovar_ru:
            if i in slovar_ru[j]:
                count = count + j
print(count)


        





























# one = A = a = E = e = I = i = O = o = U = u = L = l = N = n = S = s = T = t = R = r = 1
# three = B = b = C = c = M = m = P = p = 3
# four = F = f = H = h = V = v = W = w = Y = y = 4
# five = K = k = 5
# eight = J = j = X = x = 8
# ten = Q = q = Z = z = 10
# sum = 0
# count = 0
# slovo = input('Введите слово: ')
# for i_1 in range(len(slovo)):
#     if slovo[i_1] == (one) or (three) or (four) or (five) or (eight) or (ten):
#         slovo = (one) or (three) or (four) or (five) or (eight) or (ten)
#         count += 1
#         print(slovo[i_1])