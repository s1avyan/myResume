import random

# random
# 1. Загадать случайное число от 0 до 100
print(random.randint(0, 100))
# 2. выбрать победителя лотереи из списка
players = ["Leo", "Kate", "John", "Jakie", "Sammuel", "Ahmed"]
print(random.choice(players))
# 3. выбрать трех победителей из списка

print(random.sample(players, 3))
# 4. перемешать карты в списке
cards = ["6", "7", "8", "9", "10", "T", "J", "K", "Q"]
print(cards)
random.shuffle(cards)
print(cards)
