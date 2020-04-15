cities = {'Las Vegas', 'Paris', 'Moscow'}
print(cities)
cities.add('Burma')
print(cities)
cities.add('Moscow')
print(cities)

cities.remove('Moscow')
print(cities)

print(len(cities))
print('Paris' in cities)
for city in cities:
    print(city)

#Семейная пара собирается в отпуск
# каждый из супругов берет вещи
# Макс взял
max_things ={'Телефон', "Бритва", "Рубашка", "Шорты"}
# Кейт взяла
kate_things = {'Телефон', "Зонтик", "Шорты", "Помада"}
# Какие вещи взяли супруги?
print(max_things | kate_things)
# какие вещи повторяются?
print(max_things & kate_things)
# какие вещи не взял Макс но взяла Кейт?
print(max_things - kate_things)
# какие вещи взяла Кейт но не взял Макс
print(kate_things - max_things)