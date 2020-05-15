# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:22:29 2020

@author: HaoNinghui
"""

#import some useful libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#change the working directory to where full_data.csv file stored
os.chdir("D:\\ZJU\\Academic\\ZJE 第一学年\\ZJE第二学期\\IBI")
#read the content of the .csv file, in dataframe object
covid_data=pd.read_csv("full_data.csv")

# show all column, every third tow between (and including)0 and 15
z=covid_data.iloc[0:16:3,:]
print (z)

#retrieving values
#covid_data.loc[every row where location is "Afghanistan","total_cases"]
 #1.read all row, just the "location" column
 #1.covi_data.iloc[:,"location"]
 #2.create Boolean, True when Afghanistan,False when others
a = pd.DataFrame(covid_data)
b = [0 for i in range(len(a))]
for i in range(len(a)):
    if covid_data.iloc[i,1] == 'Afghanistan':
        b[i] = True
    else:
        b[i] = False


covid_data.iloc[b,:]
#check that it is the same as covid_data.loc[0:81,'total_cases']

#worldwide situation
world_new_cases=[]
world_dates=[]
world_new_deaths=[]
#retriveing the data
a = pd.DataFrame(covid_data)
c = [0 for i in range(len(a))]
for i in range(len(a)):
    #selecting the data that satisfy location==World, 'date''new_cases'columns
    if covid_data.iloc[i,1] == 'World':#first standard
        world_new_cases.append(covid_data.iloc[i,2])#second
        world_dates.append(covid_data.iloc[i,0])#third
        world_new_deaths.append(covid_data.iloc[i,3])
#need not use True and False because we createnow objects, just give them data
worldmean=np.mean(world_new_cases)
worldmedian=np.median(world_new_cases)
print (worldmean)
print (worldmedian)
#we may also use world_new_cases.discribie to see the mean & median

#1.The mean and median are different. mean is higher than median and this means 
#2.new cases of these day are increasing rapidly because the mean value is mucher higher than
#the median value, new cases of median date is not that much while afterwards new cases is more. 

#plot the new cases as a box plot
plt.title('new cases around the world')
plt.ylabel('new cases')
plt.boxplot(world_new_cases,
            showcaps = 'world new cases',
            vert = True,
            meanline = True,
            whis = 1.5,
            patch_artist = True,
            showbox = True,
            notch = False)
plt.show()
#this plot fit the interpretation i made referring to mean and median.
#After reaching the peak, new cases may gradually decrease

#plot data over time
#new cases
plt.plot(world_dates,world_new_cases,'b+',label='world new cases')
#plt.plot(world_dates,world_new_deaths,'r+')
#plt.plot(world_dates,world_new_deaths,'ro')
#plt.plot(world_dates,world_new_deaths,'bo')
#'b' refers to color blue(r to red),'+' refers to the shape of the point
plt.title('new cases and new deaths around the world' )
plt.xlabel('date')
plt.ylabel('number of cases')
plt.xticks(world_dates[0:len(world_dates):4],rotation=-90)
   #iloc is undefined so I delete it but do not understand
   #every four the date is rotated 90 degrees to show themselves clearly
#new deaths
plt.plot(world_dates,world_new_deaths,'r+',label='world new deaths')
plt.legend()
plt.show()

#Question part
#number of new cases and deaths in Kenya and Colombia over the time
K_newcases=[]
K_dates=[]
C_newcases=[]
C_dates=[]
a = pd.DataFrame(covid_data)
c = [0 for i in range(len(a))]
for i in range(len(a)):
    if covid_data.iloc[i,1] == 'Kenya':
        K_newcases.append(covid_data.iloc[i,2])
        K_dates.append(covid_data.iloc[i,0])

for i in range(len(a)):
    #selecting the data that satisfy location==World, 'date''new_cases'columns
    if covid_data.iloc[i,1] == 'Colombia':
        C_newcases.append(covid_data.iloc[i,2])
        C_dates.append(covid_data.iloc[i,0])

plt.plot(K_dates,K_newcases,'b+',label='Kenya new cases')
plt.title('new cases in Kenya and Colombia' )
plt.xlabel('date')
plt.ylabel('number of cases')
plt.xticks(K_dates[0:len(world_dates):3],rotation=-90)
plt.plot(C_dates,C_newcases,'r+',label='Colombia new cases')
plt.legend()
plt.show()