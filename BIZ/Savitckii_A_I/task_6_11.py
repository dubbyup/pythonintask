﻿# Задача 6. Вариант 11.
# Создайте игру, в которой компьютер загадывает название одного из девяти действующих вокзалов Москвы, а игрок должен его угадать.

#Savitckii A I
#14.04.2017

import random
x=random.choice(["Казанский вокзал", "Курский вокзал", "Ленинградский вокзал", "Белорусский вокзал", "Павелецкий вокзал", "Киевский вокзал","Савеловский вокзал","Рижский вокзал","Ярославский вокзал"])
print ("Назовите один из девяти вокзалов Москвы.")
name=input("Ваш вариант: ")

if name==x:
	print("Правильно!")
else:
	print ("Не угадал!")


input("\n\nНажмите Enter для выхода.")