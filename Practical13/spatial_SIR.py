# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:38:49 2020

@author: HaoNinghui
"""
#import necessary library
import numpy as np
import matplotlib.pyplot as plt
#make arrat of all sescepible population
population=np.zeros((100,100))
#use population [4,12] to check the number in row 4, column 12 

outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1

plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')
#set up model parameters
beta=0.3#independent now
gamma=0.05 #infected people recover probobility
#every time the infected will acount how many neighbors
#what is the ratio that touched neighbors will get infected
#