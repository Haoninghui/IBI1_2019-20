# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:36:13 2020

@author: HaoNinghui
"""
#input the integer
m=eval(input("input a positive integer smaller than 8192:"))
#give another variable the value of input number used in last step
n=m
#define 'result'
result=""
#because input number is smaller than 2**13=8192
#which makes the code much easier to begin at j=13
j=13
#2**0=1 so m!=0 is an general condition(like True).
while m!=0:
    #compare input number with 2**j to judge the first item(other items)of the string
    if m>=2**j:
        m-=2**j
        #we further calculate the remaining part of the number,so we minus 2**j from m
        if m!=0:
            result+="2**"+str(j)+"+"
            #we define the result as a sequence(a sentence formed by parts using '+')
        else:
            result+="2**"+str(j)
        #we calculate the next item which is 2**(j-1)
        #give j the value of j-1
        j-=1
    else:#just jump to the next step
        j-=1

#Finally we output/print the result.
print(str(n)+"is"+result)
    
    