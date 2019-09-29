import math
a = float(input('Введите первое число:'))
b = float(input('Введите второе число:'))
amin = math.ceil(min(a, b)) # Ставим округление к большему на случай если пользователь введет диапазон 4.3 5.2
bmax = int(max(a, b))
c = list(range(amin -1, bmax + 1)) # Так как range() срезает последнее число +1, так как итератор + 1 то  берем для нашего исчесление последнее число -1
for i in c:
    i += 1
    if i < 1: # Отсекаем числа меньше ноля.
        continue
    elif i > bmax: # Если привышает bmax то цикл обрывается
        break
    else:
        print(i)
else:
    print('else')
