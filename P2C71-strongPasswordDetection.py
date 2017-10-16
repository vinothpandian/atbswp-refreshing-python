#! python

import re

# strongPasswordRegEx = re.compile(r'''^
#     (?=.*[a-z])
#     (?=.*[A-Z])
#     (?=.*\d)
#     [a-zA-Z\d]{8,}
#     $''')

lowerRegEx = re.compile(r'(?=.*[a-z])')
upperRegEx = re.compile(r'(?=.*[A-Z])')
digitRegEx = re.compile(r'(?=.*\d)')
lengthRegEx = re.compile(r'[a-zA-Z\d]{8,}')

print("Please enter your password : ", end='')
password = input()

strength = 0

if lowerRegEx.match(password):
    strength += 1

if upperRegEx.match(password):
    strength += 1

if digitRegEx.match(password):
    strength += 1

if lengthRegEx.match(password):
    strength += 1

PASSWORD_STRENGTH = {
    1: "low yo!",
    2: "okish...",
    3: "nearly perfect but not quite there yet...",
    4: "perfectly awesome!"
    }

if strength == 0:
    print("Please type something sensible!")
else:
    print("Your password strength is "+PASSWORD_STRENGTH[strength])
