print('Добрый день, Вы зашли в программу которая поможет высчитать площадь и переметр прямоугольника, начнем:') # Добавил приветствие и пояснения, что бы программа выглядела более дружелюбно.
a = float(input('Введите одну сторону прямоугольника: ')) # Так как функция input делает 'a' и 'b' строками, используем float() что бы перевести в тип числа.
b = float(input('А теперь введите вторую сторону: '))

c = 2 * (a + b) # Прописываем формулы.
d = a * b

print('\nПериметр прямоугольниака равен: ', c) # Перенес на следующую строку что бы был более приятный вывод.
print('Площадь прямоугольника равна:', d)
input("Нажмите \'Enter\' для завершения.") # Добавил еще один ввод что бы пользователь успевал увидеть результат.
