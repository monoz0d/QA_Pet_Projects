from random import randrange
def is_valid(num, border):
    return 1 <= int(num) <= border
print('Добро пожаловать в числовую угадайку')
while True:
    z = int(input('Введите правую границу диапазона: '))
    x = randrange(1,z+1)
    counter = 1
    while True:
        n = input(f'Введите число от 1 до {z}: ')
        if not is_valid(n, z):
            print(f'А может быть все-таки введем целое число от 1 до {z}')
            continue
        else:
            n = int(n)
            if n < x:
                counter += 1
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif n > x:
                counter += 1
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif n == x:
                print('Вы угадали, поздравляем!')
                print('Количество попыток:', counter)
                break
    y = input('Хотите сыграть еще раз? ')
    if y.lower() == 'да':
        continue
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break