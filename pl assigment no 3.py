# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:05:38 2026

@author: GAURI
"""

# Program to check whether a number is even or odd

# Taking input from the user
num = int(input("Enter a number: "))

# Checking condition
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# Program to check greatest out of three numbers

# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Checking conditions
if a >= b and a >= c:
    print(f"{a} is the greatest")
elif b >= a and b >= c:
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")

# Program to check whether a character is uppercase or lowercase

# Taking input from the user
ch = input("Enter a character: ")

# Checking condition
if ch.isupper():
    print(f"{ch} is Uppercase")
elif ch.islower():
    print(f"{ch} is Lowercase")
else:
    print(f"{ch} is not an alphabet character")
# Program to check whether input is a number or character

# Taking input from the user
ch = input("Enter something: ")

# Checking condition
if ch.isdigit():
    print(f"{ch} is a Number")
elif ch.isalpha():
    print(f"{ch} is a Character")
else:
    print(f"{ch} is neither a pure number nor a character")
