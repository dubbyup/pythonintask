# Задача 4. Вариант 7.
# Напишите программу, которая выводит имя, под которым скрывается Мария Луиза Чеччарелли.
# Дополнительно необходимо вывести область интересов указанной личности, место рождения,
# годы рождения и смерти (если человек умер), вычислить возраст на данный момент
# (или момент смерти). Для хранения всех необходимых данных требуется использовать
# переменные. После вывода информации программа должна дожидаться
# пока пользователь нажмет Enter для выхода.

# Lysenko N.A.
# 23.03.2017

print ('Мария Луиза Чечарелли, более известна, как итальянская актриса Мо́ника Ви́тти.')
place = 'Рим, Италия'
print ('Место рождения: ', place)
year = 1931
old = 2017 - year
print ('Год рождения: ', year)
print ('Возраст: ', old)
prof = 'игра ролей в фильмах, написание сценариев, кинорежиссура'
print ('Область интересов: ', prof)

input ('\n\nНажмите Enter для выхода.')
