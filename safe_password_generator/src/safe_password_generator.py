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
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = lowercase_letters.upper()
punctuation = '!#$%&*+-=?@^_'
chrs = ''
a = int(input('Введите количество паролей для генерации: '))
b = int(input('Введите длину одного пароля: '))
c = input('Включать ли цифры? ')
chrs += verify(c, digits)
d = input('Включать ли строчные латинские буквы? ')
chrs += verify(d, lowercase_letters)
e = input('Включать ли прописные латинские буквы? ')
chrs += verify(e, uppercase_letters)
f = input('Включать ли символы !#$%&*+-=?@^_? ')
chrs += verify(f, punctuation)
g = input('Исключать ли неоднозначные символы il1Lo0O? ')
if f.lower() == "да":
    for i in chrs:
        if i in 'il1Lo0O?':
            chrs = chrs.replace(i, '')
for _ in range(a):
    print(generate_password(b, chrs))