# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с помощью input()
# А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False


# Добавил метод .lower(), что бы не иметь привязки к регистру, но данный метод мы пока не изучали

word = input("Введите слово латинскими буквами: ").lower() # Запрос ввода слова у пользователя

a = word.count("a") # Проверяем количество букв "a" и присваиваем переменную
e = word.count("e") # Проверяем количество букв "e" и присваиваем переменную
i = word.count("i") # Проверяем количество букв "i" и присваиваем переменную
o = word.count("o") # Проверяем количество букв "o" и присваиваем переменную
u = word.count("u") # Проверяем количество букв "u" и присваиваем переменную

sum = a + e + i + o + u # Складываем значения переменных гласными
print("Всего гласных букв: ", sum) # Выводим на экран общее количество гласных букв
print()
print("Из них: ")

if word.count("a") != 0: # Добавляем условие, что если значение переменной не равно ноль
    print("Букв 'a': ", a) # То печатаем значение из этой переменной
else: # В других случаях, т.е. по сути, когда нет гласных букв
    print("Букв 'a': ", int(a) != 0) # Выводим на экран False, можно обойтись просто функцией print(), но я думаю в этом задании хотят именно этого

if word.count("e") != 0:
    print("Букв 'e': ", e)
else:
    print("Букв 'e': ", int(e) != 0)

if word.count("i") != 0:
    print("Букв 'i': ", i)
else:
    print("Букв 'i': ", int(i) != 0)

if word.count("o") != 0:
    print("Букв 'o': ", o)
else:
    print("Букв 'o': ", int(o) != 0)

if word.count("u") != 0:
    print("Букв 'u': ", u)
else:
    print("Букв 'u': ", int(u) != 0)