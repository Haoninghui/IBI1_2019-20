# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:19:51 2020

@author: HaoNinghui
"""
#This is similar with what we learnt in high school.(Tossing and turning)

#Words after 'input' is an indication for operator to input the integer
#'eval'function foramts the input to number.
x=eval(input("input a positive integer x="))

print("{} is".format(x),end="")
j=0
while x!=0:
    a=x%2
    x=(x-a)/2
    if a==1:
        if j==0:
            print("2**0",end="")
        else:
            print("+2**{}".format(j),end="")
    j+=1