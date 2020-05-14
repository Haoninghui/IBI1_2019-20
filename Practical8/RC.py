# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:27:52 2020

@author: HaoNinghui
"""

seq='ATGCGACTACGATCGAGGGCCAT'
#first reserve the provided sequence
def DNA_reserve(a):
    return a[::-1]

#define a function to calculate complementary sequence
def DNA_complementary(sequence):
    #develop a complementary dictionary
    comp_dict={"A":"T","T":"A","C":"G","G":"C"}
    #trans sequence string into list (to convert to their complementary base)
    sequlist=list(sequence)
    #change to their complementary base
    sequlist=[comp_dict[i]for i in sequlist]
    # assemble the elements(list) in sequlist into string
    b=''.join(sequlist)
    return b
#calculate the given sequence
b=DNA_reserve(seq)
c=DNA_complementary(b)
print ("The reserve complementary string is ",c)