# # 1 Даны два произвольные списка.
# # Удалите из первого списка элементы присутствующие во втором списке.
# my_list_1 = [2, 2, 2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3, 4]
#
# result = set(my_list_1) - set(my_list_2)
#
# print(set(my_list_1))
# print(set(my_list_2))
# print(list(result))
#
# # my_list_1 = [1, 1, 1, 1, 2, 3, 4, 5, 5, 5, 5]
# # my_list_2 = [1, 2, 3, 4]
# # my_list_1_copy = my_list_1
# #
# # for number in my_list_1[:]:
# #     if number in my_list_2:
# #         my_list_1.remove(number)
#
# print(my_list_1)
# 2 Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача — вывести дату в текстовом виде,
# например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


date = '02.11.2013'
d, m, y = date.split('.')


day = {
    '01': 'Первое',
    '02': 'Второе',
    '03': 'Третье',
    '04': 'Четвертое'
}
month = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '11': 'ноября'
}
result = f'{day[d]} {month[m]} {y} года'
print('-> ',day,month,y)

print('-> ',result)
# print(day_letter,month_letter[month-1], year, 'года')

# 3: Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
my_new_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_new_list_1_set = set(my_new_list_1)
print(my_new_list_1_set | my_new_list_1_set)

list1 = [2, 8, 8, 8, 2, 5, 12, 8, 2, 12]
result = []
for number in list1[:]:
    if list1.count(number) == 1:
        result.append(number)

print(result)