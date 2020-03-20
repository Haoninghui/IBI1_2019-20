# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:43:14 2020

@author: HaoNinghui
"""

 #Give a number to process


# set function to process n
def collatz(number):
    r = number % 2
    if r == 0:
        return number // 2
    else:
        return 3 * number + 1

# while-loop to display the results
while n !=1:
    print(collatz(n))
    n = collatz(n)
