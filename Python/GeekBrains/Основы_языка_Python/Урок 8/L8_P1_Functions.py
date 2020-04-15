def hello(who):
    print('Hello', who)

hello('Max')

def hello(who, say='Hello'):
    print(who, say)

hello('Max')

def greeting(say, *who):
    print(who, say)

hello('Max')


def print_sep(sep, sep_len):
    print(sep * sep_len)

print_sep('*', 50)

numbers = []

for i in range (3):
    number = int(input('Введите любое число: '))
    numbers.append(number)

def print_L8P1(a):
    minim = min(a)
    maxim = max(a)
    summ = sum(a)
    print(f'Минимальное значение - {minim}; максимальное - {maxim}; сумма всех чисел - {summ}.')

print_L8P1(numbers)

