print('Соревнования по гребле лопатами в огороде')
count = int(input("Введите, сколько человек приняли участие?: "))
athlets = []

while count > 0:
    name = input('Кто занял {} место: '. format(count))
    athlets.append(name)
    count-=1

winners = athlets[-1:-3]
print(winners)
print('В соревнованиях участвовали: ', sorted(athlets))
athlets.reverse()
winners = athlets[:3]
print(winners)

#result = 'Победители: первое место {}, второе место {}, третье место {}. Поздравляем!!!'.format(place_1.upper(), place_2.upper(), place_3.upper())
result = 'Победители: {}. Поздравляем,'.format(winners)
print(result)