# За день машина проезжает n километров. Сколько дней нужно, чтобы 
# проехать маршрут длиной m километров? При решении этой задачи нельзя 
# пользоваться условной инструкцией if и циклами.
# **Input:**
# n = 700
# m = 750


n = int(input('Сколько проезжает машина в день:'))
m = int(input('Сколько нужно проехать: '))
# print(f'{(m//n)+1} дня')
s = (n + m - 1) // n
print(s)