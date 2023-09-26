# Select the scret number from a given range.
#Player must guess the number.
# Compare guess to the scret number.
# What happens if the guess is wrong?
    # Tell them the guess is wrong.
    # Tell them the number of guesses left.
    # Tell them if too high / too low.
# What happens if the guess is right?
    # tell them guess is correct.
    # Award a point.
    # What happens if the player runs out of guesses?
    # Tell player round has been lost.
    # Award point to CPU.
# Check to see if player or CPu has >= 3 points if so they win.

import random # Import the random module to our code.

# DECLARATIONS
secretNumber = -1
playerGuess = -1
playerScore = 0
cpuScore = 0
numGuesses = 0
playerName = ""
difficulty = ""
rangeMin = -1
rangeMax = -1
numAttempts = -1
difficulty = ""

print("""
        *~~~~~~~~~~~~~~~~~~~~~~~~~*
        |                         |
        |     Guess a Number      |
        |    Truitte Moreland     |
        |           2023          |
        *~~~~~~~~~~~~~~~~~~~~~~~~~*
        
        """)

# CPU SECRET NUMBER GENERATION
secretNumber = random.randint(0,20)
#print(secretNumber)

# GAME LOOP
print("You need to guess a number from 0 to 20 and you have four guesses. \nIf you guess it right, you")
# ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH MATCH.
# print() an explantion of your three difficulty levels.
# Use input() to store difficulty in difficulty variable.
# assign values to numAttempts, and rangeMin, and rangeMin, and rangeMax based on choice.

while playerScore != 3 and cpuScore != 3: # START THE MATCH (GAME)
    # Difficulty code needs to be BEFORE the round starts.
    # pass -- Tells Python to skip this block of code.

    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    secretNumber = random.ranint(rangeMin, rangeMax)
    # Whenever you assign a spevifiv value to something, it's called "hard coded".
    #print(secretNumber)
    # ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH ROUND.
    #Difficulty levels go 1-3
    difficulty = "Easy"
    print("This is easy mode you have 2 guesses to guess a number 1-3")
    difficulty = "Meduim"
    print("This is meduim mode you have 5 guesses for numbers 1-15")
    difficulty = "Hard"
    print("This is so hard mode you have 4 guess to guess a number 1-25")
    
    
    
    numGuesses = 0
    for guesses in range(4): # START THE ROUND!
        # PUT DIFFICULTY CODE 
        print(f"You have {4 - numGuesses} guesses remaining. \n")
        playerGuess = input("Type a number from 0 to 20 and press ENTER.sss\n")
        # input() saves all data as a STRING by defualt.
        # int() will convert to an INTERGER
        # float() will convert to a FLOAT
        print(f"You have chosen {playerGuess}. Let's see if you're right!\n")
        if playerGuess == secretNumber:
            print("Whoa dude, what a guess! You got it!\n")
            playerScore += 1
            break # IMMEDIATELY EXIT ANY LOOP YOU ARE IN!
        else: 
            if playerGuess > secretNumber:
                print("Your guess is too high.\n")
            else:
                print("Your guess is too low")
        numGuesses += 1
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU wins a point since you ran out of guesses.\n")

if playerScore >= 3:
    print("Winner, winner, chicken dinner! You scored 3 points first!\n")
else:
    print("Yo, you lost to a computer. You are a scrub. \n")

