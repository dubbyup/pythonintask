# Задача 6. Вариант 5
# Создайте игру, в которой компьютер загадывает один из трех цветов светофора, а игрок должен его угадать.

# Евграшина А.В.
# 16.04.2017

print ("Угадайте цвет светофора")
import random
цвет=random.choice (["красный", "желтый", "зеленый"])
if цвет == input('Введите цвет: '):
	print ("Вы угадали!")
else:
	print ("Вы не угадали!")


input("\n\nHaжмитe Enter. чтобы выйти.")