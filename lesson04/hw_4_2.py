# Ввод текста.
def input_text():
    print('Если хотите выйти из программы просто нажмите "Enter"') #Выносим принты за цыкл что бы оно не повторяло каждый раз.
    print('Если хотите подсчитать статистику введеного текста. Введите текст:')
    some_list = [] # Cоздаем пустой лист который будем наполнять.
    while True:
        text = input().lower() # С помощью lower сравниваем большие и маленькие буквы(Делает все в нижнем регистре).
        print("Для подсчета статистики после ввода текста нажите (Enter)")
        if text != "":
            some_list.append(text) # Заполняем наш список. введеным текстом.
        else:
            return some_list # Возвращаем все в список.

def text_stat(text):
    text2 = list(''.join(text)) # Используем join() чтобы каждый символ был выделен в отдельно, иначе мы не сможем посчитать Статистику символов.
    print("Всего строк = ", len(text)) # Используем Len Для подсчета
    count_numbers(text2) # Вызываем функцию подсчета цифр.
    count_symbols(text2) # Вызываем функцию подсчета Символов.
    count_word(text) # Вызываем функцию Подсчета слов.

# Считаем цифры.
def count_numbers(text2):
    count = 0
    for i in text2:
        if i.isdigit() == True: # С помощью isdigit() отбираем только числа.
            count += 1
    print("Всего цифр = ", count) # Выводим количество цифр.


# Считаем символы
def count_symbols(text2):
    chars = {} # Создаем пустой словарь который.
    for unique_symbols in text2: # Наполняем наш словарь через конструкцию for...in
        if unique_symbols in chars:
            chars[unique_symbols] += 1 # Если символ уже есть в словаре то плюсуем 1.
        else:
            chars[unique_symbols] = 1 # Если символа нету (второй раз) то делаем единичку.
    key_list = list(chars.keys()) # метод .keys() возвращает список всех используемых ключей в произвольном порядке
    key_list.sort() # теперь для сортировки применяем метод.sort()
    print("<--- Статистика символов ---") # Открываем начало границы(обозначения) ипользую что бы было как в примере.
    for key in key_list: # с for key in chars.items(): меняем на  for key in key_list:
        print("{} = {}".format(repr(key), chars[key])) # Меняем вывод.
        # вставляем сюда еще repr()  что бы у нас отображалось ключи со скобками (на подобии примера).
    print("--- Статистика символов --->") # Закрываем границы(обозначения) ипользую что бы было как в примере.

# Подсчет уникальных слов
def count_word(text):
    words_stat = {} # Создаем кортеж который будем наполнять.
    separate_list = [] #Создаем лист который будем наполнять.
    for _value in text: # Делаем из того что ввел пользователь список
        next_value = _value.split() #делаем новый лист в котором Используем split() как разделитель
        separate_list = separate_list + next_value #плюсуем
    for unique_words in separate_list: #Подсчитываем повторения и теперь считаем уже слова через words_stat
        if unique_words in words_stat:
            words_stat[unique_words] += 1 # Если встречается несколько раз тогда плюсуем 1 за каждое повторение
        else:
            words_stat[unique_words] = 1 # Если один раз встречается присваеваем 1
    key_list = list(words_stat.keys()) # метод .key() возвращает список всех используемых ключей в произвольном порядке
    key_list.sort() # теперь для сортировки применяем метод.sort()
    print("<--- Статистика слов ---") #Есть описание выше.
    for key, value in words_stat.items():
        print("{} = {}".format(repr(key), value))
    print("--- Статистика слов --->")


text = input_text()
text_stat(text)