#!/usr/bin/env python
# coding: utf-8

# In[2]:


#dsependencies
import os
import pandas as pd


# In[3]:



#pull in csv data
filepath = "Resources/budget_data.csv"
df = pd.read_csv(filepath)
df.head()


# In[35]:


#number of months
monthCount = df["Date"].count()
print(monthCount)


# In[13]:


#total P&L over the period
totalPandL = int(df["Profit/Losses"].sum())
print(totalPandL)


# In[47]:


#find change by month
averageChange = df["Profit/Losses"].diff()
averageChange.head()

df["Monthly Change"] = averageChange
df.head()

#find average change over the whole period
avgMonthlyChange = df["Monthly Change"].mean()
print(avgMonthlyChange)


# In[29]:


#find max monthly change in the dataset
maxPosition = df["Monthly Change"].idxmax()
print(maxPosition)
df.iloc[maxPosition,0]


# In[28]:


#find min monthly change in the dataset
minPosition = df["Monthly Change"].idxmin()
print(minPosition)

#print month using iloc
df.iloc[minPosition,0]


# In[69]:


#printing final analysis
def printFinal():
    print("Financial Analysis")
    print("--------------------------------------")
    print("Total Months: " + str(monthCount))
    print("Total: $" + str(totalPandL))
    print("Average Change: $" + str(round(avgMonthlyChange,2)))
    print("Greatest increase in profits: " + str(df.iloc[maxPosition,0]) + " ($" + str(df.iloc[maxPosition,1]) + ")")
    print("Greatest increase in profits: " + str(df.iloc[minPosition,0]) + " ($" + str(df.iloc[minPosition,1]) + ")")
printFinal()


# In[81]:


total_file = ("Bank Results.txt")

with open(total_file,"w",) as file:
    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write("Total Months: " + str(monthCount))
    file.write("\n")
    file.write("Total: $" + str(totalPandL))
    file.write("\n")
    file.write("Average Change: $" + str(round(avgMonthlyChange,2)))
    file.write("\n")
    file.write("Greatest increase in profits: " + str(df.iloc[maxPosition,0]) + " ($" + str(df.iloc[maxPosition,1]) + ")")
    file.write("\n")
    file.write("Greatest increase in profits: " + str(df.iloc[minPosition,0]) + " ($" + str(df.iloc[minPosition,1]) + ")")
    
total_file = ("Bank Results.txt")


# In[ ]:




