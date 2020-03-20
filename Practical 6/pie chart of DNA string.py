# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 07:18:56 2020

@author: HaoNinghui
"""

#Develop a pie chart to show the data
#pie chart
import matplotlib.pyplot as plt

labels='A','G','C','T'#name of 4 parts
sizes=[6,5,4,6]#indicate the ratio
explode=[0,0,0,0]#internal between each part
plt.pie(sizes,explode=explode,labels =labels,autopct='%1.1f%%',
        shadow=False,startangle=90)
plt.axis('equal')
plt.title('pie of the four DNA nucleotides')
plt.show()