# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:01:49 2020

@author: HaoNinghui
"""
#define a if calculate loop to calculate the next number of the sequence
def collatz(number):
    #if the integer is even
    if number % 2 == 0:
        #the next number is half of the previous number
        return number / 2
    #if the integer is odd
    else:
        #the next number is the result of the equation
        return 3 * number +1
    

#int let the input number be integer
#words after input is the hint to input the number.
number = int(input("positive integer:"))
while True:
    number = collatz(number)
    print(str(number))
    if number == 1:
        break
    
print(str(number))
