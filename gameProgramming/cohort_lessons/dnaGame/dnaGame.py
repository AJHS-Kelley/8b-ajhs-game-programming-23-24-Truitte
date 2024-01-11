# DNA Replication Game, Ryan Kelley, v0.0

# Import Entire Modules -- Get the whole tool box.
import time, datetime 

# Import Specific Methods -- Get the specific tool.
from random import choice

# Store the DNA Bases
dnaBases = ["A", "T", "G", "C"]

# GAME FUNCTIONS
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive integer number of bases to generate.\n"))
    dnaSequence = ""

    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence

# dna = genDNA()
# print(dna)

def genRNA(dnaSequence: str) -> tuple:
