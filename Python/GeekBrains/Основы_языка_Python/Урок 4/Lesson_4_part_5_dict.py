#dictionary

friend = {
    'name': 'Max',
    'age': 23,
    'has_car':  True
}
#Перебор словаря по ключам. метод "keys"
for key in friend.keys():
    print(key)
    print(friend[key])

for key in friend:   #Метод ".keys" является методом по умолчанию
    print(key)
    print(friend[key])
#Перебор по значениям. пренебрегая ключами
for var in friend.values():
    print(var)
#Перебор по парам ключ/значение.
for item in friend.items():
    print(item)

    for key, val in friend.items():
        print(key, val)