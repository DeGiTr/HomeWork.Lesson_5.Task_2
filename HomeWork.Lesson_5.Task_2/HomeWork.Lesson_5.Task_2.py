# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с помощью input()
# А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False

word = input("Введите английское слово: ")

a = word.count("a")
e = word.count("e")
i = word.count("i")
o = word.count("o")
u = word.count("u")

sum = a + e + i + o + u
print(sum)