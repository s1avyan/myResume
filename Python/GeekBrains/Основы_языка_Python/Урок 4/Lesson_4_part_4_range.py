#Применение функции RANGE
friends = ['James', 'Tifany', "John"]

numbers = [1, 3, 5]
for number in numbers:
    print(number)

print(list(range(0, 51, 5)))

for number in range(0, 51, 5):
    print(number)

for winner in friends:
    print(winner)

for i in range(len(friends)):
    print(i+1, ')', friends[i])