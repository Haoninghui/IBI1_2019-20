# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:36:13 2020

@author: HaoNinghui
"""

m=eval(input("input a positive integer smaller than 8192:"))
n=m
result=""

j=13
while m!=0:
    if m>=2**j:
        m-=2**j
        if a!=0:
            result+="2**"+str(j)+"+"
        else:
            result+="2**"+str(j)
        j-=1
    else:
        j-=1

print(str(n)+"is"+result)
    
    