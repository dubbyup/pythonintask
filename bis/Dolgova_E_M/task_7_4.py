﻿# Задача 7. Вариант 4.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Dolgova E. M.
# 29.03.2017

import random
x=random.choice(["Убийство Немейского льва ", "Борьба с Лернейской гидрой", "Стимфалийские птицы", "Керинейская лань", "Эриманфский кабан", "Авгиевы конюшни", "Критский бык", "Кони Диомеда", "Бой с амазонками", "Бой с Герионом", "Цербер", "Борьба с Антеем"])
print ("Назовите один из двенадцати подвигов Геракла.")
y=10
while y>0:
	name=input("Ваш вариант: ")
	if name==x:
		print("Правильно!")
		break
	else:
		print ("Не угадал!")
		y=y-1
		continue
print("Количество очков =", y)

input("\n\nНажмите Enter для выхода.")
