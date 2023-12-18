# Python Performance Monitoring Module by Truitte Moreland, v0,0
import time

def execStart():
    startTime = time.time()
    return startTime

def execStop():
    stopTime = time.time()
    return stopTime

def execTime(startTime, stopTime):
    return f"Exuction Time: {startTime - stopTime} seconds.\n"





