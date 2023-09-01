import random

WORDS = ('hello', 'apple', 'car', 'fixture',)
MAX_GUESSES = 3
RESPONSE_CONDITION = False

print('Welcome!')
print('You have to find the word within', MAX_GUESSES, 'guesses.')
print()

word = random.choice(WORDS)
scrambled_word = ''.join(random.sample(word, len(word)))

for guess in range(MAX_GUESSES):
    print('Scrambled word is:', scrambled_word)
    answer = input('Enter you guess: ')

    if answer == word:
        print('Well done!')
        RESPONSE_CONDITION = True
        break
    else:
        print("Sorry, wrong answer")

if not RESPONSE_CONDITION:
    print('GAME OVER.The word was:', word)
