import math
a = float(input('Введите первое число:'))
b = float(input('Введите второе число:'))
amin = math.ceil(min(a, b)) # Ставим округление к большему на случай если пользователь введет диапазон 4.3 5.2
bmax = int(max(a, b))
z = list(range(amin, bmax + 1)) #Делаем список для генератора 
zc = [1*i for i in z if i > 0]
cz = sum(zc)
print(zc) # Выводим список натуральных чисел в заданом пользователем диапазоне.
print('Сумма всех натуральных чисел', cz) #Выводим сумму натуральных чисел. (Это задание со звездочкой, вывести сумму).