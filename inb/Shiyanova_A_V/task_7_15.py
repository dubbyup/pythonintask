#Задание 7. Вариант 15.
#1-50. Разработайте систему начисления очков для задачи 6, в соответствии
#с которой игрок получал бы большее количество баллов за меньшее количество
#попыток.

#Shiyanova A.V.
#22.03.2017
import random
print('Программа загадывает один из городов, входящих в Золотое кольцо России, а пользователю предоставляется возможность отгадать загаданный город')
porks= ('Радонеж','Сергиев Посад','Александров','Владимир','Боголюбово','Гороховец','Суздаль','Кидекша','Гусь Хрустальный','Орехово','Юрьев Польский','Переславль-Залесский')
computer =porks[random.randint(0,2)]
score = 100
while score != 0:
    user = (input('Угадайте какой город загадал компьютер: '))
    if user == computer:
        print ('Верно!Это',computer)
        print ('Вы получаете', score, 'очков,(Максимально Вы можете получить 100 очков)')
        break
    elif score == 50:
        print ('К сожалению у Вас закончились попытки, вы получаете 0 очков(')
    else:
         print ('К сожалению вы не угадали, попробуйте еще раз')
    score -= 50
input ('Нажмите Enter для выхода')