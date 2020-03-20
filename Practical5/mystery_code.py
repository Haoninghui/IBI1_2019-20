# What does this piece of code do?
# Answer: To select a number that cannot be devided into integer except 1 and itself
#         In other words, the code randomly output the prime number including 1 from 1 to 100.
# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
#selcet a random number from 1 to 100
    n = randint(1,100)
#define u is the possible integer factor of n in the middle of all possible factors
    u = ceil(n**(0.5))
    for i in range(2,u+1):#includes 2 to u
#if n can be divided into integer by i 
        if n%i == 0:
            p=False
#I find that if we write
            #if n%i!=0:
            #p= False
        #the out put will be 1,2,4,6,12(i haven't find it out)

     
print(n)
