# Задача 6. Вариант 19.
# Создайте игру, в которой компьютер загадывает название одного из семи городов России, имеющих действующий метрополитен, а игрок должен его угадать.
# Tyshlek D.N.
# 18.04.2017

import random

print("Программа случайным образом загадывает имя одного из семи городов, а игрок должен угадать его.")

number = random.randint(1,7)

if number == 1:
    city = "Москва"
elif number == 2:
    city = "Санкт-Питербург"
elif number == 3:
    city = "Сочи"
elif number == 4:
    city = "Раменское"
elif number == 5:
    city = "Домодедово"
elif number == 6:
    city = "Волгоград"
elif number == 7:
    city = "Краснодар"

answer = input("Назовите один из городов России: ")

if answer == city:
    print("Вы угадали!")
else:
    print("Вы не угадали!")
    print("Правильный ответ: ", city)

input("\nНажмите Enter для выхода.")