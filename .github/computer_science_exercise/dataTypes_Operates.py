#Data type and Opreraters, Truitte Moreland, V0.5

#Variable Rules
#CANNOT START WITH A NUMBER
#CANNOT USE BUILT- IN KEYWORDS AS VARIABLES
#VARIABLE NAME SHOULD DESCRIBE THE DATA BEING STORE.
#snake_case variables use _ to seperate words, all lower case.
#Camelcase variables do not use spaces, 1st word lower, rest up

# String Literal Examples
playerName = "Jack Love"
emptyString = ""
spaceString = " "
monsterName = "Purple People eater"

#INTERGER data types
health = 100
extralives = 5
temperature = -17

# Floating Point Data Types
pi = 3.1415678 
lapTime = 3.5
velocity = -2.0

#Boolean Data Types
isFireType = False
weaponEquipped = True
pvpEnabled = False

# Arithmetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH CLASS!
print(3 + -1) # Addition
print(0 - 25) # Subtraction
print(1 * -1) # Multiplication 
print(3 / -1) # Division
print(3 ** 4) # Exponents
print(18 % 4) # Modulus --

# Comparison Operators
#Evaluate the expression, then returm True or False
print(5 > 3) # Greater Than 
print(7 >= 1) # Greater Than or equal to
print(-1 < -2) # Less Than
print(0 <= 0) # Less than or equal to
print(5 ==3) # Equal to
print(-99 != 99) #Not equal to

# Assignment Operators
myVariable = 'myValue' #Assign variable on the left the value on the right, throw out my current values
myOtherVariable = (10 + 5)

myVariableAgain = 1
myVariableAgain = 5
print(myVariableAgain)

#Addition Assingment -- Add the value on the right, keeping any current value
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet)

# Same Effect
x= 0
x+= 1 
x = x + 1

# Logical Operators 
 print (3 > 5 and 4 < 3) #And requires All expressions to be True.
 print( 3 > 2 and 4 < 3)
 print (3 > 2 and 4 != 3)
 print (3 > 2 and 4 != 3 and favColor == "Blue" and temp == -5)
 # when writing and expressions. put the value most liokely to be False first!
 
 # Logical OR -- Requires ONE expression to be True.
 print(5 > 2 or 2 < -2)
 print(3 != 3 or 5 == 5)

 # AND OR Combined
 print("Line 81")
 print(3 > 2 and 4 < 3 or 5 != 7)
 print( True and False or True)

# NOT Logical Operator
print(not (3 > 2))
print(not (not (not (5 != 3))))
