#! python

import sys

def collatz(num):
    if num%2 == 0:
        return num//2
    else:
        return (num*3)+1

try:
    print('Enter your number :',end='')
    num = int(input())
except ValueError:
    print("That's not a number!")
    sys.exit()

while num != 1:
    num = collatz(num)
    print(num)
