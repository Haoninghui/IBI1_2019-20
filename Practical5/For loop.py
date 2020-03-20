# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:00:53 2020

@author: HaoNinghui
"""
n=25

def collatz(n):
    a=n%2
    if a==0:
        return n/2
    else:
        return n*3+1
    
while n!=1:
    print(collatz(n))
    n=collatz
