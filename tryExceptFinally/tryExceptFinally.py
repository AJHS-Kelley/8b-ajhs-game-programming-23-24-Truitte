# This is a method for testing code and preventing crashes.
# try -- except -- else -- finally

try: # The code in this block is ALWAYS executed
    myVariable = 1
    print(myVariable)
    myString = "Five"
    print(float(myString))
except NameError: # This code will run IF there is an error (exeption)
    print("There is an incorrect variable name in your code.")
except:
    print("Something else went wrong.")
else: # This code runs if there are NO ERRORS
    print("Code executed correctly with no exceptions.\n")
finally: # THIS CODE ALWAYS RUNS, IT'S LIKE THE TERMINATOR
    print("I'll be back.\n")