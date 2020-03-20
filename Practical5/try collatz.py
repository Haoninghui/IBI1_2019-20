# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 09:31:34 2020

@author: HaoNinghui
"""




    #input a positive integer
    n=25
def collatz(n):
    #judge whether it is odd or even
    if n%2==0:
        return n/2
    else:
        return n*3+1
        
#stop when first appear 1
while n==1:
    print(collatz(n))
    n=