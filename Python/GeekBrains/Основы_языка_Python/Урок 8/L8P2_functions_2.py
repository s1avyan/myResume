numbers = [5, 3, 2, 4, 7]

print(list(map(lambda x: x ** 2, numbers)))


print(list(map(lambda x: str(x), numbers)))

""" 
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
def is_even(number):
    return number % 2 == 0


result = filter(is_even, numbers)
print(result)
result = list(result)
print(result)

names = ["Max", "Leo", "Kate"]


def more_than(name_len):
    return name_len


print(list(filter(lambda names: len(names) > 2, names)))
 """
# numbers = [1,4,2,5,7,3,89,15,56]
#
# print(sorted(numbers, reverse=True))
#
# names = ['Andrey', 'John', 'Arnold']
#
# print(sorted(names))
#
# def by_count(city):
#     return city[1]
#
# cities = [('Москва', 1000), ('Лас-Вегас', 500), ('Антверпен', 2000)]
#
# print(sorted(cities, key=by_count))
# print(sorted(cities, key=lambda city: city[1]))

#
# numbers = range(16)
#
# def my_filter(numbers, function):
#     result = []
#     for number in numbers:
#         if function(number):
#             result.append(number)
#     return result
#
#
# def is_chet(number):
#     return number % 2 == 0
#
# def is_nechet(number):
#     return number % 2 != 0
#
# def more_than(number):
#     return number > 4
#
# print(my_filter(numbers, is_chet))
# print(my_filter(numbers, is_nechet))
# print(my_filter(numbers, more_than))
#
# print(my_filter(numbers, lambda number: number % 2 == 0))
