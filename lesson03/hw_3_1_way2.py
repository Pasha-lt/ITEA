def calc(a):
    a = abs(a) # Если пользователь введет число минус abs возьмет модуль
    res = 1 # Вводим счетчик и ставим на нем 1
    a = int(a / 10) # Определяем сколько целых раз у нас число используем обычное деление на 10 отсекаем запятую смомощью int()
    while a > 0: # если после деление получили >0 цикл запускается еще раз и отсекает еще одну цифру
        a = int(a / 10)
        res +=1 # Когда у нас исполняется цикл while счетчик плюсует единицу
    print(res)

while True:
    a = int(input("Введите число и вам выдаст сколько в нем цифр"))
    calc(a)