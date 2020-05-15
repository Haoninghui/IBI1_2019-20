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