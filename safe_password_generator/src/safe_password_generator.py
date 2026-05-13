from random import choice
def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += choice(chars)
    return password
def verify(answer, chars):
    while True:
        if answer.lower() == "да":
            return chars
        elif answer.lower() == 'нет':
            return ''
        else:
            answer = input('Некорректный ввод, попробуйте еще раз: ')
def main():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = lowercase_letters.upper()
    punctuation = '!#$%&*+-=?@^_'
    chrs = ''
    try:
        a = int(input('Введите количество паролей для генерации: '))
        b = int(input('Введите длину одного пароля: '))
    except ValueError:
        print("Ошибка: количество и длина должны быть числами!")
        return
    c = input('Включать ли цифры? ')
    chrs += verify(c, digits)
    d = input('Включать ли строчные латинские буквы? ')
    chrs += verify(d, lowercase_letters)
    e = input('Включать ли прописные латинские буквы? ')
    chrs += verify(e, uppercase_letters)
    f = input('Включать ли символы !#$%&*+-=?@^_? ')
    chrs += verify(f, punctuation)
    g = input('Исключать ли неоднозначные символы il1Lo0O? ')
    if g.lower() == "да":
        for i in "il1Lo0O":
            chrs = chrs.replace(i, '')
    if not chrs:
        print("Ошибка: Вы не выбрали ни одного набора символов!")
        return
    for _ in range(a):
        print(generate_password(b, chrs))
if __name__ == '__main__':
    main()