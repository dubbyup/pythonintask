#Задача 9. Вариант 8.
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен
#его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять  
#попыток узнать, есть ли какая-либо буква в слове, причем программа может
#отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать
#слово.

#Krotkova V.D
#20.04.2017

import random

#создадим последовательность слов, из которых компьютер будет выбирать
WORDS = ("яблоко", "персик", "тыква", "игрушка", "свинья", "огурец")

#случайным образом выберем из последовательности одно слово
word = random.choice(WORDS)
attempt = 0 #количество попыток узнать букву

#создадим переменную, с которой будет сопоставлена версия игрока
correct = word
#создадим строку, которая будет содержать все буквы слова
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
#создадим строку, в которой буту отгаданные игроком буквы
letters = ""

#начало игры
print(
"""
        Добро пожаловать в игру "Угадай слово"!
    У вас есть 5 попыток узнать, есть ли какая-либо буква в слове,
    после чего вы должны угадать слово.
  (Для выхода нажмите Enter, не вводя своей версии.)
"""
)
print('В загаданном слове ', len(correct) , 'букв.')
guess = input('\nПопробуйте угадать какую-либо букву: ')
attempt += 1
while attempt < 5 and guess != "":
    if guess in jumble:
        print('Да, такая буква есть в загаданном слове.')
        letters += guess     
    else:
        print('Нет, такой буквы в слове нет.')
    attempt += 1
    guess = input('Попробуйте еще раз: ')
print('К сожалению, попытки отгадать букву закончились.\n')
print('Буквы, которые вы угадали: ', letters)
answer = input('Попробуйте отгадать все слово: ')
if attempt == 5 and answer != "":
    if answer == correct:
        print('Верно! Поздравляю, вы выиграли!')
    else:
        print('Неверно! К сожалению, вы проиграли!')
print('Загаданное слово : ', correct)
print('Спасибо за игру.')
input('\n\nНажмите Enter, чтобы выйти.')


    
