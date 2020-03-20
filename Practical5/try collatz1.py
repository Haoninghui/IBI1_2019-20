# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:01:49 2020

@author: HaoNinghui
"""

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number +1
    
number = int(25)
while True:
    number = collatz(number)
    print(str(number))
    if number == 1:
        break
print(str(number))
