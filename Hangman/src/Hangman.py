import random
words = ['пока', 'анаконда', 'москва', 'ящерица']
def get_word():
    return random.choice(words).upper()
def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      0
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      0
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      0
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      0
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      0
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      0
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]
def play(word):
    guessed_letters = []
    guessed_words = []
    word_progress = ['_'] * len(word)
    tries = 6
    print('Давайте играть!')
    print(display_hangman(tries))
    print(f'Слово: {"".join(word_progress)} ({len(word)} букв)')
    while tries > 0 and '_' in word_progress:
        guess = input('Введи букву или слово: ').upper()
        if not guess.isalpha():
            print('Введите только буквы!')
            continue
        if len(guess) > 1:
            if guess in guessed_words:
                print('Вы уже пробовали это слово!')
                continue
            guessed_words.append(guess)
            if guess == word:
                word_progress = list(word)
                break
            else:
                print('Слово неверное 😢')
                tries -= 1
        else:
            letter = guess
            if letter in guessed_letters:
                print('Эта буква уже была!')
                continue
            guessed_letters.append(letter)
            if letter in word:
                print('Есть такая буква!')
                for i in range(len(word)):
                    if word[i] == letter:
                        word_progress[i] = letter
            else:
                print('Такой буквы нет 😢')
                tries -= 1
        print('Слово:', ''.join(word_progress))
        print('Буквы:', guessed_letters)
        print(display_hangman(tries))
    if '_' not in word_progress:
        return '🎉 Вы победили!'
    return f'💀 Вы проиграли. Слово было: {word}'
print(play(get_word()))