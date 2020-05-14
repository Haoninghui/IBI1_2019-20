# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:47:06 2020

@author: thinkpad
"""

s = input(r"Please input integers between 1 to 23 to compute 24points: (Please use ',' to divide them)")
#can be changed by the function'append'
num = []
for item in s.split(","):#do not need string
   num.append(float(item))
#in case that the unput is larger than 24
   #stop when flag==False
flag = False
while flag == False:
    flag = True
    for item in num:
        if ((item > 23) or (item < 1)):# not suitable for our game
            flag = False
            print("One of the invalid number is" + str(int(item)) + ", which should be between integers 1 to 23.")
            #ask users to input other 4 numbers (same as previous 8 to 12 lines )
            s = input(r"Please input numbers to compute 24: (Please use ',' to divide them)")
            num = []           
            for item in s.split(","):
                num.append(float(item))
            break
            
   
# calculate & List all possible situations
def cal(l: int):
   return_list = []
   for i in list(range(l-1)):
      for j in list(range(i+1,l)):
          for k in range(6):
        #refers to input number, change their *form*
             return_list.append([i, j, k])
   return (return_list)#save the result
   

#remain two numbers to further calculation
sc = [[], []]
for i in range(2, len(num) + 1):
   sc.append(cal(i))
   
all_sit = []
all_sit_tmp = []
sci = []
for i in range(len(num)):
   sci.append(sc[len(num) - i])
   
# Select one operation [] from one stage.  
def select_copy(l: list):
   l_copy = l.copy()
   if len(l_copy) == len(sci) - 1:
      all_sit.append(l_copy)
   for item in sci[len(l)]:
      l.append(item)
      select_copy(l)
      l.pop()
   
select_copy([])
 
# Apply in a define function to do the calculation
def f(i:int, j:int, k:int, l:list):
    if (k == 0):
        value = l[i] + l[j]
    elif (k == 1):
        value = l[i] - l[j]
    elif (k == 2):
        value = l[j] - l[i]
    elif (k == 3):
        value = l[i] * l[j]
    elif (k == 4) and (l[j] != 0) :
        value = l[i] / l[j]
    elif (k == 5) and (l[i] != 0):
        value = l[j] / l[i]
    else:
        value = 0
    #after calculation we got 24 then result is 1(self-choice)
    if (value == 24):
        return (1)
    else:
        l[i] = value
        l.pop(j)
        return (-1)

#final precess: develop a loop to output the result
a = 1   #develop 'a'  as a measurement to judge whether input could obtain 24 after calculation(no matter what sepcific value)
n = 1   #develop 'n' to represent operation time
for item in all_sit:
   num_copy=num.copy()
   #try to calculate until goes to 'a=-1'
   for jtem in item:
       if (f(jtem[0], jtem[1], jtem[2], num_copy) == 1 ) and a == 1:
          print("Yes")
          print("Operation time: " + str(n))
          a = 0
       else:
          n += 1 #add one operation time
if a == 1: #'a' still equals to 1 indicating there is no answer
    print("No")

#there still somewhere to improve!!!!!
#1. different input order may lead to different operation time
#2. the operation time is possible not the least operation time, for example if I input 1,3,5,4
    #operation time & different order of numbers
    #2190  3,4,5,1
    #165   1,3,4,5
    #56    1,5,4,3
    #30    5,4,1,3