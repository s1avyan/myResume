import random
number = random.randint(1,100)
print(number)
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input('Выберите уровень сложности от 1 до 3: '))
max_count = levels[level]

user_count = int(input('Введите количество пользователей: '))
users = []
for user in range(user_count):
    user_name = input(f'Введите имя пользователя {user}')
    users.append(user_name)

print(users)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('Все пользователи проиграли')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            print(f'Поздравляем! Победил {user}')
            is_winner = user
            break
        elif number < user_number:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
print(f'Понадобилось {count} попыток')