# Control Flow, Ryan Kelley, v0.0
# DECLARATIONS

favColor = "Red"
luckyNumber = 7
myGPA = 3.47
myAge = 16
pineappleOnPizza = False

# if Statements - Check for a condition to be True/False, do something if true.
if favColor == "Red":
    print("I like your style.")

    if luckyNumber == "7":
        print("Truittes the best soccer player")

# if-else Statement -- Check for a condition, do something for True and False
if myGPA >= 3.0:
    print("Congratulations on making the honor roll!")
else:
    print("Better luck next year.  Try to study more!")

if myGPA >= 3.0:
    print("Congratulations on making the honor roll!")
else:
    print("Better luck next year.  Try to study more!")

# if - elif - else Statements -- Checks for multiple conditions
if myAge > 65:
    print("Congratulations on retiring!")
elif myAge > 50:
    print("Congratulations, you have earmed a bonus of $1000!")
else:
    print("You are not old enough for a bonus.")
# 1 if, 1 else, any number of elif allowed.

























# while Loop -- Think 'MUSICAL CHAIRS" -- used when you do NOT know how many iterations you need.
# iteration = one complete trip through a loop
x = 0
while x < 100:
    print(f"X is currently equal to {x}")
    x += 1

while x >= 0:
    print (f"X is currently equal to {x}")
    x -= 1

# for Loop -- Think 'Go Fish', used when you know number of iterations needed.
print("For LOOP STARTS HERE")
for i in range(10): # i = iterable variable
    print(i)

print("EVEN OR ODD LOOP!")
for i in range(101):
    print(i)
if i % 2 == 0:
    print("That number is even!")
    else:
        print("That number is odd!")


# () Parentheses
# [] Square Brackets
# <> Angle Bracets
# {} Braces