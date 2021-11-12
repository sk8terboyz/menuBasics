from fractions import Fraction
import math

# Turing Test
def turingTest():
    ignore = input("What is your problem?")
    response = input("Have you had this problem before (yes or no)?")
    if response == "yes":
        print("Well you have it again.")
    elif response == "no":
        print("Well, you have it now.")
    else:
        print("That wasn't 'yes' or 'no' so I cannot respond properly.")

def tempConverter():
    temp = int(input("Enter your temperature in Farenheit "))
    converted = round((temp+32) * Fraction(5,9))
    degreeSign = u"\u00b0"
    print(temp,degreeSign,"F =",converted,degreeSign,"C")

def hypotenuse():
    a = int(input("What is a = ? "))
    b = int(input("What is b = ? "))
    c = math.sqrt((a**2)+(b**2))
    formatC = "{:.2f}".format(c)
    print("The hypotenuse is",formatC)

# Menu
def menu():
    request = int(input("Which would yo like to test?\n(1) Turing Test\n(2) Temperature Converter\n(3) Hypotenuse\n"))
    if request == 1:
        turingTest()
    elif request == 2:
        tempConverter()
    elif request == 3:
        hypotenuse()
    else:
        print("You did not an option. Terminating")
menu()