# -*- coding: utf-8 -*-
"""
Created on Sat May 13 21:14:21 2017

@author: ghisalhasan
"""

#List of questions:
#1. Do players neglect their weight more the older they get?
#2. Is the height and weight of players inversely proportional?
#3. Did Teams began hiring tall players selectively at the last decades?


#Importing necessary mods
import thinkstats2
import thinkplot
import numpy as np
import pandas as pd

#Opining Masters file
file = open('Master.txt', 'r')

text = file.readlines()

#Initializing lists
names = []
weights = []
heights = []
newtext = []
birth = []
#To skip the labels of the columns
skip = True
for row in text:
    if skip == True:
        skip = False
        continue
    #Splitting the text
    row = row.split(',')
    #Adding elements to each list
    names.append(row[0])
    weights.append(row[16])
    heights.append(row[17])
    birth.append(row[1])

    newtext.append(row)
    
    
    
#Numbering for the dataframe
ind = range(1,19106)
#Making frequency list
birthfreq = {}
#Jumping years in 10's.
years = range(1800,2010,10)
for birthyear in birth:
    for year in years:
        #Checking if the person's birthyear is known, and if the year is smaller than the one being checked
        if birthyear.isdigit() and int(birthyear) < year:
            #Adding to dictionary
            birthfreq.setdefault(years[years.index(year) -1],0)
            birthfreq[years[years.index(year)-1]]+=1
            break
     
        

#Repearing the same thing with weights
weightfreq = {}

weightnums = range(100,300,10)
for weight in weights:
    for num in weightnums:
        if weight.isdigit() and int(weight) < num:
            weightfreq.setdefault(weightnums[weightnums.index(num) -1],0)
            weightfreq[weightnums[weightnums.index(num)-1]]+=1
            break
        
        
#Repearing the same thing with heights
heightfreq = {}
heightnums = range(60,85,2)
for height in heights:
    for num in heightnums:
        if height.isdigit() and int(height) < num:
            heightfreq.setdefault(heightnums[heightnums.index(num) -1],0)
            heightfreq[heightnums[heightnums.index(num)-1]]+=1
            break
        

#Making database of important lists as columns
database = {'Name' : pd.Series(names, index=ind),'Weight' : pd.Series(weights, index=ind),'Height' : pd.Series(heights, index=ind),'Birth Year' : pd.Series(birth, index=ind)}
#Creating dataframe
df = pd.DataFrame(database)
#___________________________________

#Plotting histograms

#Plotting histogram of Weight
hist = thinkstats2.Hist(weightfreq)
hist
thinkplot.Hist(hist)
thinkplot.Show(xlabel='Weight', ylabel='Frequency')

#Plotting histogram of Height.
hist = thinkstats2.Hist(heightfreq)
hist
thinkplot.Hist(hist)
thinkplot.Show(xlabel='Height', ylabel='Frequency')

#Plotting histogram of Birthyear frequencies
hist = thinkstats2.Hist(birthfreq)
hist
thinkplot.Hist(hist)
thinkplot.Show(xlabel='Birth year', ylabel='Frequency')

#___________________________________

#Plotting CDF's

#Plotting CDF of Weight
Cdf = thinkstats2.Cdf(weightfreq)
thinkplot.Cdf(Cdf)
thinkplot.Show(xlabel='Weight', ylabel='CDF')

#Plotting CDF of Height
Cdf = thinkstats2.Cdf(heightfreq)
thinkplot.Cdf(Cdf)
thinkplot.Show(xlabel='Height', ylabel='CDF')

#Plotting CDF of birth years
Cdf = thinkstats2.Cdf(birthfreq)
thinkplot.Cdf(Cdf)
thinkplot.Show(xlabel='Birth Year', ylabel='CDF')
#___________________________________

#Plotting PMF's

#Plotting PMF of Weight
Pmf = thinkstats2.Pmf(weightfreq)
thinkplot.Pmf(Pmf)
thinkplot.Show(xlabel='Weight', ylabel='PMF')

#Plotting PMF of Height
Pmf = thinkstats2.Pmf(heightfreq)
thinkplot.Pmf(Pmf)
thinkplot.Show(xlabel='Height', ylabel='PMF')

#Plotting PMF of Birth Year
Pmf = thinkstats2.Pmf(birthfreq)
thinkplot.Pmf(Pmf)
thinkplot.Show(xlabel='Birth Year', ylabel='PMF')



#Plotting CCDF of Weight
Cdf = thinkstats2.Cdf(weightfreq)
thinkplot.Cdf(Cdf, complement = True)
thinkplot.Show(xlabel='Weight', ylabel='CCDF')


#Cleaning weights and birthyears from empty cells of both sides even if only one of them was empty
cleanweights = []
cleanbirth = []

for index in range(0,len(weights)):
        if weights[index] == '' or birth[index] == '':
            continue
        else:
            cleanweights.append(int(weights[index]))
            cleanbirth.append(int(birth[index]))
            
#Defining jitter method to generate predictions, and make the plot look more natural
def Jitter(values, jitter=0.5):
    n = len(values)
    return np.random.uniform(-jitter, +jitter, n) + values

#Using the jitter function
birth = Jitter(cleanbirth, 1)
weights = Jitter(cleanweights, 1)
#Plotting the scatterplot
thinkplot.Scatter(birth, weights, alpha=0.05)
thinkplot.Show(xlabel='Birth Year',ylabel='Weight (pounds)')



