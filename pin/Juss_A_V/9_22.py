#Задача 9.Вариант 22
#Создайте	игру,	в	которой	компьютер	выбирает	какое-либо	слово,	а	игрок	должен его	отгадать.	Компьютер	сообщает	игроку,	сколько	букв	в	слове,	и	дает	пять	попыток узнать,	есть	ли	какая-либо	буква	в	слове,	причем	программа	может	отвечать	только "Да"	и	"Нет".	Вслед	за	тем	игрок	должен	попробовать	отгадать	слово.
#Juss A.V.
#19.04.2017

import random

WORDS = ("стакан","рука", "отвертка", "душ", "телевизор", "программа", "очки", "голова")

word = random.choice(WORDS)

print("У вас есть 5 попыток угодать букву, а я скажу есть ли она в загаданном мною слове. После 5 попыток вы должны отгадать посностью все слово.")
print("Кол-во букв в слове - ", len(word))

attempt = 5

while attempt>0:
    letter = input("Угадайте одну из букв в загаданном слове: ")
    attempt -= 1
    if letter in word:
        print("Буква ", letter, " есть в слове.")
    else:
        print("Буквы ", letter, " нет в слове.")

guess = input("Угадайте загаданное слово: ")
if guess == word:
    print("Правильно!")
else:
    print("Не правильно! Загаданное слово -", word)