#!/usr/bin/env python3
"""evelandy/W.G.
July 16 2018 9:21pm
Simple-Calculator
Python36-32
uses command line to calculate
simple commands
"""
while True:
    print("To add press +: ")
    print("To subtract press -: ")
    print("To multiply press *: ")
    print("To divide press *: ")
    print("To quit press Q: ")

    I = input("")

    if I == 'Q':
        print("Ending program")
        break
    if I != '+':
        if I != '-':
            if I != '*':
                if I != '/':
                    if I != 'Q':
                        print("Please enter a valid operator")
                        break
        

    x = (float(input("Enter your first number: ")))
    y = (float(input("Enter your second number: ")))


    if I == '+':
        print(x + y)
    elif I == '-':
        print(x - y)
    elif I == '*':
        print(x * y)
    elif I == '/':
        print (x / y)
    else:
        print("Please run again with valid characters")
        break
