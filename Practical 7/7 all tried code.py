# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:38:02 2020

@author: HaoNinghui
"""

#import some useful libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#change the working directory to where full_data.csv file stored
os.chdir("D:\\ZJU\\Academic\\ZJE 第一学年\\ZJE第二学期\\IBI")
#show the currrent working directory
os.getcwd
#list all the directory in the current working directory
os.listdir

#read the content of the .csv file, in dataframe object
covid_data=pd.read_csv("full_data.csv")
# reading part of data
covid_data.head(5)
 #5 indicates the first 5 lines of data in the .csv (not including the very first line)
#closer look in the full_data.csv 
covid_data.info()
 # data type: first two columns are object, last four are integers
 # columns: date, location, new_cases, new_death,total_cases, total_deaths
 #7996 rows
#show the number of entries, mean, standard deviation, a number of quantiles
covid_data.describe()
 #mean of new cases: 193.546773, median: 0.000000
 #range of total deaths: max 37272.000000, min 0.000000
#see only sepcific values(1 column, 1 row)
 #counting begins at ZERO!
covid_data.iloc[0,1]
 #[row,column]
 
# show all column, every third tow between (and including)0 and 15
covid_data.iloc[0:16:3,:]

#loc
covid_data.loc[2:4,"date"]
 #row:234, column: date
 
#look for rows that interested without knowing the row number
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
print(b)

covid_data.iloc[b,:]
#check that it is the same as covid_data.loc[0:81,'total_cases']

#Prepare for part 4:6 
world_dates = []
world_new_cases = []
world_new_deaths = []
for i in range(len (a)):
    if covid_data.iloc[i,1] == 'World':
        world_new_cases.append (covid_data.iloc[i,2])
        world_dates.append (covid_data.iloc[i,0])
        world_new_deaths.append(covid_data.iloc[i,3])
# Part 4
world_mean = np.mean(world_new_cases)
world_median = np.median (world_new_cases)
print (world_mean)
print (world_median)
# Part 5
plt.title('new cases in the world')
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
# Part 6
plt.title('new cases in the world')
plt.xlabel('new cases')
plt.ylabel('date')
plt.plot(world_dates, world_new_cases, 'b+')
plt.xticks(world_dates[0:len(world_dates):4],rotation=-90)
plt.show()
plt.title('new deaths in the world')
plt.xlabel('new deaths')
plt.ylabel('dates')
plt.plot(world_dates, world_new_deaths, 'b+')
plt.xticks(world_dates[0:len(world_dates):4],rotation=-90)
plt.show()

# Question
China_dates = []
China_new_cases = []
China_total_cases = []
for i in range(len(a)):
    if covid_data.iloc[i,1] == 'China':
        China_dates.append (covid_data.iloc[i,0])
        China_new_cases.append (covid_data.iloc[i,2])
        China_total_cases.append(covid_data.iloc[i,4])
plt.title('new cases in China')
plt.boxplot(China_new_cases,
            showcaps = 'China new cases',
            vert = True,
            meanline = True,
            whis = 1.5,
            patch_artist = True,
            showbox = True,
            notch = False)
plt.show()
plt.plot(China_dates, China_new_cases, 'b+')
plt.title('new cases in China')
plt.xlabel('new cases')
plt.ylabel('dates')
plt.xticks(China_dates[0:len(China_dates):6],rotation=-90)
plt.show()
plt.title('total cases in China')
plt.xlabel('total cases')
plt.ylabel('dates')
plt.plot(China_dates, China_total_cases, 'b+')
plt.xticks(China_dates[0:len(China_dates):6],rotation=-90)
plt.show()