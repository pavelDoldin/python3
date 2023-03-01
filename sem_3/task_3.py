# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит
        # Первое решение
# listOfDictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007"}]
# list = []
# for i in listOfDictionary:
#     for j in i.values():
#         if j not in list:
#             list.append(j)
# print(list)
        # Второе решение
spisok = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"},
{" VIII ": "S007"}]
result = list()
for dict in spisok:
    for k in dict:
        result.append(dict[k])
print(set(result))