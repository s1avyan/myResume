import random
min_number = int(input('Введите нижний предел диапазона чисел: '))
max_number = int(input('Введите верхний предел диапазона чисел: '))

user_number = int(input(f'Введите число между {min_number} и {max_number}: '))
print(user_number)
comp_number = None
count = 0

while comp_number != user_number:
    count += 1
    print(f"Компьютер предпринимает {count} попытку угадать число")
    comp_number = random.randint(min_number, user_number)
    print(f"Число компьютера: {comp_number}")
    result = input('Введите сравнение с вашим числом: "<" ">" "=" :')
    if result == '=':
        print('Компьютер угадал число')
        break
    elif result == '<':
        print('Загаданное число больше')
        min_number = comp_number
    else:
        print("Загаданное число меньше")
        max_number = comp_number