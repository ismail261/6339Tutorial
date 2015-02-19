# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 21:49:20 2015

@author: Ismail
"""

# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to importa library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import os
import numpy as np

df = pd.read_csv('D:\\books\\semester 5\\Special topics in advanced DB\\tutorial\\pandas\\Cse-6339-crime.csv')
#print(df[['DATE  OF OCCURRENCE','Street','PRIMARY DESCRIPTION']][:10])

#primary reason for crime and their count

# general describe
#print(df['PRIMARY DESCRIPTION'].describe())

#print(df['PRIMARY DESCRIPTION'].value_counts())

#plot crime and count
#df['PRIMARY DESCRIPTION'].value_counts()[:8].plot(kind='bar')

#plot streets and count
#df['Street'].value_counts()[:8].plot(kind='bar')

#common location for crime theft to occur
isPriDesc = df['PRIMARY DESCRIPTION'] == 'THEFT'
df1 = df[isPriDesc]
#print(df1['LOCATION DESCRIPTION'].value_counts())

# total crimes for combination of primary reason and location
df2 = pd.crosstab(df['PRIMARY DESCRIPTION'],df['LOCATION DESCRIPTION'])
#df2.to_csv('D:\\books\\semester 5\\Special topics in advanced DB\\tutorial\\pandas\\croosTab_Total.csv')

# How many arrested for different crimes
df2 = pd.crosstab(df['PRIMARY DESCRIPTION'],df['ARREST'])
#df2.to_csv('D:\\books\\semester 5\\Special topics in advanced DB\\tutorial\\pandas\\croosTab_Arrest.csv')

#df2.plot(kind='bar')

# How many arrested for different crimes
df2 = pd.crosstab(df['PRIMARY DESCRIPTION'],[df['ARREST'],df['DOMESTIC']])
#df2.to_csv('D:\\books\\semester 5\\Special topics in advanced DB\\tutorial\\pandas\\croosTab_Arrest_Domestic.csv')
df2.plot(kind='bar')