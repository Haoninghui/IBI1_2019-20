# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:08:02 2020

@author: HaoNinghui
"""

def powerof2(n):
    m=13
    if n%2**m<n:
        x=x+2**m
        m=m-1
        return n=n%2**m
    else:
         m=m-1
         return n
     
n=int(input("integer number:"))        
while True:
      n=powerof2(n)
      print(str(x))
      if m==0:
          break
     