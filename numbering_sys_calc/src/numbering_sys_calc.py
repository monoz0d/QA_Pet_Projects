digits = '0123456789ABCDEF'
def calc_10(number, base):
    number = number.upper()
    new_number = 0
    for char in number:
        new_number = new_number * base + digits.index(char)
    return new_number
def calc_n(number, base):
    if base == 2:
        return bin(number)[2:]
    elif base == 8:
        return oct(number)[2:]
    elif base == 16:
        return hex(number)[2:].upper()
    new_number = ''
    while number > 0:
        new_number += digits[number % base] + new_number
        number //= base
    return new_number
def input_verify():
    while True:
        base = int(input('Введите систему счисления (2–16): '))
        if 2 <= base <= 16:
            return base
        print('Ошибка')
def calc_initiation():
    while True:
        mode = input('Переведем в десятичную систему или из десятичной? (1 - в дес., 2 - из дес.): ')
        if mode == '1':
            return calc_10(input('Введите число: '), input_verify())
        elif mode == '2':
            return calc_n(int(input('Введите число: ')), input_verify())
        print('Некорректный ввод, попробуйте еще раз: ')
print(calc_initiation())