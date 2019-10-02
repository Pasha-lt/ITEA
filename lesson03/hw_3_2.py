def nok(a,b):
    m = a*b        #Ищем нод по формуле Евклида
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    nod = a + b
    nok = m//nod
    return nok  #можно было бы прописать  print(nok) и в 16 строчке написать nok(a,b) работало б также

while True:
    try:
        a = int(input("Введите первое число"))
        b = int(input("Введите второе число"))
        print(nok(a,b))
    except ValueError:
        print('Вводить нужно цифры')
        continue
