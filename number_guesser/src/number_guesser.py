from random import randrange
def is_valid(num, border):
    try:
        num = int(num)
        return 1 <= num <= border
    except ValueError:
        return False
def get_border():
    while True:
        border = input('Введите правую границу диапазона: ')
        try:
            border = int(border)
            if border > 1:
                return border
            print("Граница должна быть больше 1")
        except ValueError:
            print('Ошибка: введите целое число')
def main():
    print('Добро пожаловать в числовую угадайку')
    while True:
        z = get_border()
        x = randrange(1,z+1)
        counter = 1
        while True:
            n = input(f'Введите число от 1 до {z}: ')
            if not is_valid(n, z):
                print(f'А может быть все-таки введем целое число от 1 до {z}')
                continue
            n = int(n)
            if n < x:
                counter += 1
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif n > x:
                counter += 1
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                print('Количество попыток:', counter)
                break
        y = input('Хотите сыграть еще раз? ')
        if y.lower() != 'да':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
if __name__ == '__main__':
    main()