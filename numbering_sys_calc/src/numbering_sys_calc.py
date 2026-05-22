digits = '0123456789ABCDEF'
def calc_10(number, base):
    number = number.upper()
    new_number = 0
    for char in number:
        new_number = new_number * base + digits.index(char)
    return new_number
def calc_n(number, base):
    if number ==0:
        return '0'
    elif base == 2:
        return bin(number)[2:]
    elif base == 8:
        return oct(number)[2:]
    elif base == 16:
        return hex(number)[2:].upper()
    new_number = ''
    while number > 0:
        new_number = digits[number % base] + new_number
        number //= base
    return new_number
def input_verify():
    while True:
        try:
            base = int(input('Введите систему счисления (2–16): '))
            if 2 <= base <= 16:
                return base
            print('Ошибка: основание должно быть от 2 до 16.')
        except ValueError:
            print("Ошибка: введите целое число.")
def calc_initiation():
    while True:
        mode = input('Переведем в десятичную систему или из десятичной? (1 - в дес., 2 - из дес.): ')
        if mode == '1':
            try:
                num = input("Введите число: ").strip()
                if not num:
                    print("Ошибка: число не может быть пустым.")
                    continue
                return calc_10(num, input_verify())
            except ValueError:
                print('Ошибка: некорректное число для выбранной системы.')
                continue
        elif mode == '2':
            try:
                num = input("Введите число: ").strip()
                if not num:
                    print("Ошибка: число не может быть пустым.")
                    continue
                return calc_n(int(num), input_verify())
            except ValueError:
                print("Ошибка: введите целое число.")
                continue
        else:
            print("Некорректный ввод, попробуйте еще раз")
def main():
    print(calc_initiation())
if __name__ == '__main__':
    main()