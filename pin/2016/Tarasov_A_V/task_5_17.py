#	Задача	5.	Вариант	17
#       Напишите	программу,	которая	бы	при	запуске	случайным	образом	отображала название	одной	из	трех	стран,	входящих	в	военно-политический	блок "Тройственный	союз".
#	Tarasow	A.	V. #	01.04.2017
import random
x="Австро-Венгрия"
y="Италия"
z="Германия"
a=random.randint(0,2)
if(a==0):
    a=x
elif a==1:
    a=y
else:
    a=z
print(a)
input("\n\nСтрана Тройственного союза, ага")