import os
import lvl_1
os.system("CLS")

print("WELCOME TO THE GAME!")
print("WHAT'S YOUR NAME?")
Name = input()
os.system("CLS")
print("Hello " + Name + " choose your level")
print("1. EASY (find number from 1-100)")
print("2. EASY PLUS (find number from 1-500)")
print("3. MEDIUM (find number from 1-100 in 6 steps)")
print("4. MEDIUM PLUS (find number from 1-200 in 7 steps)")
print()
print("PICK THE NUMBER AND LET THE GAME START")
level = int(input())

if level == 1:
    lvl_1.start()
    os.system("CLS")
    print("Gratulacje " + Name)
    print("WYGRAŁEŚ!")
    print()
    print()
    print()
    print("Wpisz 1 jeśli chcesz zagrać ponownie")
    print("Wpisz 2 aby wyjść")
elif level == 2:
    print("ROZJEBAŁO SIE")
elif level == 3:
    print("ROZJEBAŁO SIE")
elif level == 4:
    print("ROZJEBAŁO SIE")
else:
    print("Błędny numer")