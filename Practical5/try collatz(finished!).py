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
    #search on the Internet tuse this code

#int let the input number be integer
#words after input is the hint to input the number.
number = int(input("positive integer:"))
#while loop used to let the loop stop at a specific point(first appeal 1)
while True:
    #give the variable a calculated result from the previous code.
    number = collatz(number)
    print(str(number))
#Required condition that stop when first appear number1.
    if number == 1:
        break
    # caution that while loop will not stop without a stopping word.
    
print(str(number))
