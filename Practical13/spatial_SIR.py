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
size_x = 100
time=100
population = np.zeros((size_x, size_x))
outbreak = np.random.choice(range(100), 2)
#0=S 1=I 2=R
population[outbreak[0], outbreak[1]] = 1
PP=[population]
plt.figure(figsize =(12 ,8) , dpi =150)
plt.imshow ( population , cmap='viridis',interpolation= 'nearest')
plt.show()
for ttmp in range(time):
    infectedIndex = np.where(population == 1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        for xNeighbour in (x - 1, x + 1):
            for yNeighbour in (y - 1, y + 1):
                if xNeighbour != -1 and yNeighbour != -1 and xNeighbour != size_x and yNeighbour != size_x and  population[xNeighbour, yNeighbour] == 0:
                    population[xNeighbour, yNeighbour] = np.random.choice(range(2), 1, p=[1 - beta, beta])[0]
        population[x, y] = np.random.choice((1,2), 1, p=[1-gamma,gamma])[0]
    #space is important in Python( I have made many mistakes...remember!!!)
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.show()
    plt.close()