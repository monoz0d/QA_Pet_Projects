def crypt(original_text, alphabet, step0, shift, flag):
    alphabet_len = len(alphabet)
    alphabet_upper = alphabet.upper()
    for i in range(step0, shift, flag):
        crypted_text = ''
        shift_value = i % alphabet_len
        for j in range(len(original_text)):
            if original_text[j] in alphabet:
                crypted_text += alphabet[(alphabet.index(original_text[j]) + shift_value) % alphabet_len]
            elif original_text[j] in alphabet_upper:
                crypted_text += alphabet_upper[(alphabet_upper.index(original_text[j]) + shift_value) % alphabet_len]
            else:
                crypted_text += original_text[j]
        print(crypted_text)
def verify(prompt, choices, error):
    while True:
        user_input = input(prompt)
        if user_input in choices:
            return user_input
        print(error)
def shift_verify(answer, lang_len):
    while True:
        try:
            shift = int(answer)
            shift = shift % lang_len
            return shift, shift
        except ValueError:
            if answer.lower() == 'д':
                try:
                    left = int(input("Введите левую границу диапазона: "))
                    right = int(input("Введите правую границу диапазона: "))
                    return left, right
                except ValueError:
                    answer = input("Некорректный ввод диапазона, попробуйте еще раз: ")
            else:
                answer = input("Некорректный ввод шага сдвига, попробуйте еще раз: ")
def caesar_code(mode):
    if mode == '1':
        return crypt(text, lang, first_step, shft + 1, 1)
    else:
        return crypt(text, lang, - first_step, - shft - 1, - 1)
en = 'abcdefghijklmnopqrstuvwxyz'
ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
def main():
    global text, lang, first_step, shft
    text = input('Введите исходный текст: ')
    do = verify("Шифрование или дешифрование? 1 - шифр., 2 - дешифр.: ", ['1', '2'], 'Некорректный ввод режима, попробуйте еще раз: ')
    lang = en if verify("Английский или русский? 1 - англ., 2 - рус.: ", ['1', '2'], 'Некорректный ввод языка, попробуйте еще раз: ') == '1' else ru
    first_step, shft = shift_verify(input('Укажите шаг сдвига (Если диапазон - укажите "д"): '), len(lang))
    caesar_code(do)
if __name__=="__main__":
    main()