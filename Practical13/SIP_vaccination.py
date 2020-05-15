# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:09:28 2020

@author: HaoNinghui
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm#use the same nice colour scheme
plt . figure(figsize=(6,4),dpi =150)
N=10000
beta=0.3
gamma=0.05
time=1000
plt.xlabel('time')
plt.ylabel('population')
plt.title('SIR model')
for percent in range(0,100,10):
    R=int(percent*N/100)
    I=1
    S=N-I-R
    s=[S]
    i=[I]
    r=[R]
    #same as before but i chose to use the second & worked well code forms from SIR
    for tmp in range(1,time+1):
        curr_beta=beta*I/N
        s_inf=list(np.random.choice(range(2),S,p=[1-curr_beta,curr_beta])).count(1)
        S=S-s_inf
        I=I+s_inf
        i_rec=list(np.random.choice(range(2),I,p=[1-gamma,gamma])).count(1)
        I=I-i_rec
        R=R+i_rec
        s.append(S)
        i.append(I)
        r.append(R)
    plt.plot(list(range(time+1)), i, color=cm.viridis(100),label=str(percent)+'%')
    #others use this to develop different color
    #plt.plot(list(range(time+1)), i, color=cm.viridis(percent*4),label=str(percent)+'%')
plt.title("SIR model with different vaccination rates")
legend = plt.legend(loc='upper right', shadow=True)
plt.savefig("SIR_vaccination",type='png')
plt.show()
#mostly same as before
#every time figure is slightly differnet because of 'random'