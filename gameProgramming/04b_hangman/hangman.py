# Hangman Game by Truitte Moreland, v0.0
import random
words = 'pizza pasta orange ugly nasty dark light spanish kid adult number letter battle peaceful pacisifst something nothing good bad wet dry calm angry red blue green rainbow segration injustice spider'.split()
print(words)

# VARIABLE_NAMES in ALL-CAPS AND CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |
        |
        |
    =======' ' ', ' ' '
        +---+
    0   |
        |
        |
    =======' ' ', ' ' '
        +---+
    0    |
    |    |
         |
    =======' ' ', ' ' '
        +---+
    0    |
   /|    |
         |
    =======' ' ', ' ' '
    +---+
    0     |
   /|\    |
          |
    =======' ' ', ' ' '
        +---+
    0     |
   /|\    |
   /      |
    =======' ' ', ' ' '
    +---+
    0    |
   /|\    |
   / \    |
    =======''']

# Pick Word from List
def getRandomWord(wordlist): # Return a random word from the list.
    wordIndex = random.randint(0, len(wordlist) - 1)
    #len(listName) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
    return wordlist[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()
    
    blanks = '_' * len(secretWord)

    # Replace Blanks with Correct Letters
    for i in range(len(secretWord))
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + blanks[i+1:]

        for letter in blanks:
            print(letter, end = ' ')
        print()


    def getGuess(alreadyGussed):
        while True:
            print('Please guess a latter and press enter.')
            guess = input()
            guess = guess.lower()
            if len(guess) != 1:
                print('Please enter a single letter.')
            elif guess in alreadyGussed:
                print('Letter has been guessed already, try again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please guess a LETTER from the English alphabet.')
            else:
                return guess
            
def playAgain():
    print('Do you want to play again? Yes or No?')
    return input().lower(). startswith('y')

# Introduce the Game
print('Welcome to Hangman by Truitte Moreland.')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

# Main Game Loop
while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check To See If Winner, Winner Chicken Dinner
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:   # if True:
                print('Much wow! Very win!  Well done.')
                print('The secret word was' + secretWord)
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses and lost the game.')
            print('You made this number of correct guesses ' + str(len(correctLetters)))
            print('The secret word was ' + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord

            

 #i = 0
#while i < 100:
    #word = getRandomWord(words)
    #print(word)
    #i += 1