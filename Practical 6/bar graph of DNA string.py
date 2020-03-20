# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:08:22 2020

@author: HaoNinghui
"""
#using bar graph to show the number difference in DNA string
import numpy as np
import matplotlib.pyplot as plt

N=4#number of variables
scores=(6,5,4,6)
ind=np.arange(N)
width=0.38
p1=plt.bar(ind,scores,width)
plt.ylabel('percentage')#name of y axis
plt.title('number of each nucleotides')#graph title 
plt.xticks(ind,('A','G','C','T'))
plt.yticks(np.arange(3,10,1))#scale of y axis from 3 to 9(included)

plt.show()