# Задача 5. Вариант 5.
#Напишите программу, которая бы при запуске случайным образом отображала название одного из восьми соборов Московского кремля.

# Baranov K. E.
# 02.04.2017

import random

churchs = ['Колокольня Ивана Великого', 'Успенский собор', 'Благовещенский собор', 'Архангельский собор', 'Храм Положения ризы Божией Матери во Влахерне', 'Патриарший дворец и собор Двенадцати апостолов', 'Верхоспасский собор', 'Церковь Рождества Богородицы на Сенях']
n = random.randint(0, len(churchs)-1)
print(churchs[n])

input('\n\nНажмите Enter для выхода.')
