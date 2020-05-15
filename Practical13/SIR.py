# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:39:23 2020

@author: HaoNinghui
"""
#inport some necessary libraries used later in the process
import numpy as np
import matplotlib.pyplot as plt
#set up the dimensions and resolutions
plt . figure(figsize=(6,4),dpi =150)
#define some useful variables in this function
S=9999 #initial suscepible population
I=1#initial infected
R=0#initial recovery
N=S+I+R#total number 
beta=0.3
gamma=0.05
s=[S] #all can change and add new values afterwards
i=[I]
r=[R]
time=1000
for tmp in range(1,time+1):
    curr_beta=beta*I/N#this will change as infected population changed
    #choose randomly among the population
    s_inf=list(np.random.choice(range(2),S,p=[1-curr_beta,curr_beta])).count(1)
    i_rec=list(np.random.choice(range(2),I,p=[1-gamma,gamma])).count(1)
    #use other's manipulation of variables as reference 
    #initial try was all error for 'int'&'str' are not suitable in append but I change several times, it was still failed.
    s.append(S-s_inf)
    i.append(I+s_inf-i_rec)
    r.append(R+i_rec)
#define a function that easy to use when plot another figure
def plot(S,I,R):
    plt.xlabel('time')
    plt.ylabel('population')
    plt.title('SIR model')
    plt.plot(list(range(time+1)), s, 'b',label='Susceptible')
    plt.plot(list(range(time+1)), i, 'r',label='Infected')
    plt.plot(list(range(time+1)), r, 'g',label='Recovered')
    plt.legend(loc='upper right', shadow=True)
    plt.savefig("SIR stimulation",type='png')
    plt.show()

#plot the figure
plot(S,I,R)
#the first set of code is self-work but cannot develop the infected string
#here is the modified version
import numpy as np
import matplotlib.pyplot as plt
plt . figure(figsize=(6,4),dpi =150)
S=9999
I=1
R=0
N=S+I+R
beta=0.3
gamma=0.05
s=[S]
i=[I]
r=[R]
time=1000
for tmp in range(1,time+1):
    curr_beta=beta*I/N
    s_inf=list(np.random.choice(range(2),S,p=[1-curr_beta,curr_beta])).count(1)
    i_rec=list(np.random.choice(range(2),I,p=[1-gamma,gamma])).count(1)
    S=S-s_inf
    I=I+ s_inf-i_rec
    R=R+i_rec
    s.append(S)
    i.append(I)
    r.append(R)
plt.xlabel('time')
plt.ylabel('population')
plt.title('SIR model')
plt.plot(list(range(time+1)), s, 'b',label='Susceptible')
plt.plot(list(range(time+1)), i, 'r',label='Infected')
plt.plot(list(range(time+1)), r, 'g',label='Recovered')
legend = plt.legend(loc='upper right', shadow=True)
plt.savefig("SIR",type='png')
plt.show()