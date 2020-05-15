# -*- coding: utf-8 -*-
"""
Created on Wed Apr 8 00:27:52 2020

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

#another way to calculate and will be used in the task 3
s1 = ''#used in the string
seq = input('please input the DNA sequence')
for i in range(len(seq)):
#get the reserve complementary DNA sequence 
    if seq[i] == 'A':
        s1 = 'T' + s1
    elif seq[i] == 'C':
        s1 = 'G' + s1
    elif seq[i] == 'G':
        s1 = 'C' + s1
    elif seq[i] == 'T':
        s1 = 'A' + s1
    else:
        print('It is not a DNA sequence')
        break
    
if len(seq)==len(s1):#let the reserve DNA be a string 
    print(s1)