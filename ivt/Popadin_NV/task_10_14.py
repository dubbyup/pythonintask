#Задача 10.
#Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.
#Popadin N.V.
#07.04.2017

strength = 0 
health = 0 
wisdom = 0 
agility = 0 
choice = None 
global_choice = None 
while global_choice != 0: 
    points = (30 - strength - health - wisdom - agility) 
    print("Таблица характеристик на данный момент: \n" 
    " Сила: ", strength, "\n" 
    " Здоровье: ", health, "\n" 
    " Мудрость: ", wisdom, "\n" 
    " Ловкость: ", agility, "\n\n" 
    "Доступное количество очков: ", points, "\n") 
    print("Выберите пункт меню: \n" 
          "0 - Выход\n" 
          "1 - Добавить пункты к характеристике\n" 
          "2 - Уменьшить пункты характеристики\n" 
          "3 - Просмотр характеристик\n") 
    global_choice = int(input()) 
    if global_choice == 1: 
        print("К какой характеристике вы хотите добавить пункты?\n" 
              "\t\t\t1. Сила.\n" 
              "\t\t\t2. Здоровье.\n" 
              "\t\t\t3. Мудрость.\n" 
              "\t\t\t4. Ловкость.\n") 
        choice = int(input()) 
        if choice == 1: 
            print("Сколько пунктов вы хотите добавить?\n") 
            scores = int(input()) 
            if scores >= 0 and scores <= points: 
                strength += scores 
            else: 
                print("Недопустимое количество пунктов.\n") 
        elif choice == 2: 
            print("Сколько пунктов вы хотите добавить?\n") 
            scores = int(input()) 
            if scores >= 0 and scores <= points: 
                health += scores 
            else: 
                print("Недопустимое количество пунктов.\n") 
        elif choice == 3: 
            print("Сколько пунктов вы хотите добавить?\n") 
            scores = int(input()) 
            if scores >= 0 and scores <= points: 
                wisdom += scores 
            else: 
                print("Недопустимое количество пунктов.\n") 
        elif choice == 4: 
            print("Сколько пунктов вы хотите добавить?\n") 
            scores = int(input()) 
            if scores >= 0 and scores <= points: 
                agility += scores 
            else: 
                print("Недопустимое количество пунктов.\n") 
    elif global_choice == 2: 
        print("Из какой характеристики вы хотите убрать пункты?\n" 
            "\t\t\t1. Сила.\n" 
            "\t\t\t2. Здоровье.\n" 
            "\t\t\t3. Мудрость.\n" 
            "\t\t\t4. Ловкость.\n") 
        choice = int(input()) 
        if choice == 1: 
            print("Сколько пунктов вы хотите убрать?\n") 
            scores = int(input()) 
            if scores >= 0 and (strength - scores) >= 0: 
                strength -= scores 
            else: 
                print("Недопустимое количество пунктов.\n") 
        elif choice == 2: 
            print("Сколько пунктов вы хотите убрать?\n") 
            scores = int(input()) 
            if scores >= 0 and (health - scores) >= 0: 
                health -= scores 
            else: 
                print("Недопустимое количество пунктов.\n") 
        elif choice == 3: 
            print("Сколько пунктов вы хотите убрать?\n") 
            scores = int(input()) 
            if scores >= 0 and (wisdom - scores) >= 0: 
                wisdom -= scores 
            else: 
                print("Недопустимое количество пунктов.\n") 
        elif choice == 4: 
            print("Сколько пунктов вы хотите убрать?\n") 
            scores = int(input()) 
            if scores >= 0 and (agility - scores) >= 0: 
                agility -= scores 
            else: 
                print("Недопустимое количество пунктов.\n") 
    elif global_choice == 3: 
        print("Таблица характеристик: \n" 
    " Сила:", strength, "\n" 
    " Здоровье:", health, "\n" 
    " Мудрость:", wisdom, "\n" 
    " Ловкость:", agility, "\n") 
    elif global_choice == 0: 
        print("До новых встреч!") 
    else: 
        print("В меню нет такого пункта") 
input("\nНажмите Enter, чтобы выйти") 
