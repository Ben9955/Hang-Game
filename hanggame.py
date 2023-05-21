import random

print('''
This is a Hangman Game 
The Computer will randomly select a word and you need to guess the word by choosing the letters in the words. 
''')

levels = {
    'easy': 25,
    'medium': 15,
    'difficult': 8
}

guess = 0

words = ('able',
         'about',
         'account',
         'acid',
         'across',
         'addition',
         'advertisement',
         'after',
         'again',
         'against',
         'agreement',
         'air',
         'almost',
         'among',
         'amount',
         'amusement',
         'angle',
         'angry',
         'animal',
         'answer',
         'apple',
         'approval')

def check_play_again():
    choise_play_again = input('Do you want to continue playing? yes or no 🤔')
    if choise_play_again == 'yes':
        return True
    elif choise_play_again == 'no':
        return False
    else:
        return check_play_again()

def difficulties():
    global guess
    level_user = input("Select level \n" + '\n'.join([level for level in levels.keys()]))
    if level_user not in levels:
        print('Please selcet a correct level')
        difficulties()
    else:
        guess = levels[level_user]

def init():
    global current_word
    global user_state 
    difficulties()
    current_word = list(random.choice(words))
    user_state = list(len(current_word) * '_')
    print(current_word)

init()


while True:
    user_letter = input('Choose a letter in the secret word').lower()
    if user_letter.isalpha():
        if len(user_letter) != 1:
            print('Please enter one letter')
            continue
    else:
        print('Please enter just letters')
        continue
    if user_letter in current_word and current_word[-1] != user_state[-1]:
        print('Nice is correct')
        index = current_word.index(user_letter)
        user_state[index] = user_letter
        print(user_state)
        continue
    elif user_letter in current_word and current_word == user_state:
        print('Congratulation You MADE IT 😎')
        print(user_state)
        if not check_play_again():
            print('BYE 👋')
            break
        if check_play_again:
            init()

    if user_letter not in current_word and guess > 1:
        print('Wrong! Try again')
        guess -= 1
        continue

    if user_letter not in current_word and guess == 1:
        print('GAME OVER 👎👎')
        if not check_play_again():
            print('BYE 👋')
            break
        if check_play_again:
            init()

        



