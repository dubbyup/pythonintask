# Задача 4. Вариант 9.
# Напишите программу, которая выводит имя, под которым скрывается Михаил Николаевич Румянцев. Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.


# Galizin I.V.
# 22.04.2017

interes="Каранда́ш - советский артист цирка" 
print("Михаил Николаевич Румянцев более известен, как ", interes) 
PlaceOfBirth="Санкт-Петербург. СССР" 
print("Место рождения: ", PlaceOfBirth) 
YearOfBirth=("1901") 
YearOfBirth=int(YearOfBirth) 
print("Год рождения: ", YearOfBirth) 
Age=int("2017")-YearOfBirth 
print("Возраст: ", Age) 
input("Нажмите Enter для выхода.")