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

df = pd.read_csv('D:\\books\\semester 5\\Special topics in advanced DB\\tutorial\\pandas\\spring 2015 courses.csv')

#20 courses available in morning
isTime = df['Start_Am/Pm'] == 'AM'
#print(df[isTime][['Course_No','Start_Am/Pm','Name']][:20])

#classes on just friday
isDay = df['Days'] == 'Fr'
#print(df[isDay][['Course_No','Course_Name','Name']][:20])

#classes on just friday or class taken by Dimitrios Zikos
isDay = df['Days'] == 'Fr'
isName = df['Name'] == 'Dimitrios Zikos'
#print(df[isDay | isName][['Course_No','Name','Days']][:20])

#classes on friday
isDay = df['Days'].str.contains('Fr')
#print(df[isDay][['Course_No','Name','Days']][:20])

#distinct courses available
#for x in df['Course_Name'].unique():
#    print(x)

#no of classes taken by each professors
#print(df['Name'].value_counts()[:6])

#class taught by professor zikos
isName = df['Name'] == 'Dimitrios Zikos'
#print(df[isName][['Course_No','Course_Name','Name']][:20])

#descriptive statistic fors professor
#print(df['Name'].describe())

#bar graph for no of courses vs professor
df['Name'].value_counts()[:8].plot(kind='bar')



