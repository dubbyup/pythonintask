import random
lst=['банан','яблоко','груша','мандарин','слива','апельсин','абрикос','виноград']
word=random.choice(lst)
print('Приветствую тебя на игре "Угадай слово".\nПравила просты:\nТебе необходимо угадать слово, загаданное мной.\nНо перед этим даю тебе возможность пять раз угадать букву в слове.\nУдачи!')
print('В этом слове ',len(word),' букв') 
for i in range(5):
    a=input('Попробуй угадать одну из букв слова: ')
    if a in word:print('Да')
    else:print('Нет')
    print('Попробуй еще!')
y=input("а теперь попробуй угадать слово: ")
if y==word:print('Поздравляю! Ты угадал!')
else:print('К сожалению, ты не угадал, это было слово: ',word)
