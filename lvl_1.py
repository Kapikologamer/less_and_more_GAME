from multiprocessing.connection import wait
from random import randint
import time
import os

def start():
    os.system("CLS")
    for i in range(1):
        print("LOADING.")
        time.sleep(1)
        os.system("CLS")
        print("LOADING..")
        time.sleep(1)
        os.system("CLS")
        print("LOADING...")
        time.sleep(1)
        os.system("CLS")
    gameset()

def gameset():
    gameset.trynumber = int(0)
    gameset.number = randint(1, 100)
    gameview()

def gameview():
    os.system("CLS")
    print("LET'S FIND OUR NUMBER")
    print("liczba prób:")
    print(gameset.trynumber)
    game()

def game():
    shot = int(input())
    if shot > gameset.number:
        print("less")
        gameset.trynumber + 1
        time.sleep(3)
        gameview()
    elif shot < gameset.number:
        print("more")
        gameset.trynumber + 1
        time.sleep(3)
        gameview()
    elif shot == gameset.number:
        gameset.trynumber + 1

def replay():
    replay = int(input())
    if replay == 1:
        gameset()
    elif replay == 2:
        quit()
    else:
        print("Błędny numer")