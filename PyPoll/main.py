#!/usr/bin/env python
# coding: utf-8

# In[2]:


#dsependencies
import os
import pandas as pd


# In[4]:


filepath = "Resources/election_data.csv"

#pull in CSV data
df = pd.read_csv(filepath)
df.head()


# In[6]:


#total votes
totalVotes = df["Candidate"].count()
print(totalVotes)


# In[8]:


allCandidates = df["Candidate"].unique()
print(allCandidates)


# In[29]:


#find votes by candidate
khanVotes = df["Candidate"].value_counts()["Khan"]
print(khanVotes)

correyVotes = df["Candidate"].value_counts()["Correy"]
print(correyVotes)

liVotes = df["Candidate"].value_counts()["Li"]
print(liVotes)

oTooleyVotes = df["Candidate"].value_counts()["O'Tooley"]
print(oTooleyVotes)


# In[49]:


#finding percentage votes
khanPercent = (khanVotes / totalVotes)*100
print(khanPercent)

correyPercent = (correyVotes / totalVotes)*100
print(correyPercent)

liPercent = (liVotes / totalVotes)*100
print(liPercent)

oTooleyPercent = (oTooleyVotes / totalVotes)*100
print(oTooleyPercent)


# In[64]:


import operator
#create dictionary with votes
voteTotals = {"Khan":khanVotes,"Correy":correyVotes,"Li":liVotes,"O'Tooley":oTooleyVotes}
print(voteTotals)
winner = max(voteTotals.items(), key=operator.itemgetter(1))[0]
print(winner)


# In[73]:


#create list of candidates
candidateList = ["Khan","Correy","Li", "O'Tooley"]
print(candidateList)

#create a list of their vote percentages
votePercentages = [khanPercent,correyPercent,liPercent,oTooleyPercent]
votePercentages


# In[100]:


def printFinal():
    print("Election Results")
    print("---------------------")
    print("Total Votes: " + str(totalVotes))
    print("---------------------")
    print(candidateList[0] + ": " + str(round(votePercentages[0])) + "%" + "(" + str(khanVotes) + ")")
    print(candidateList[1] + ": " + str(round(votePercentages[1])) + "%" + "(" + str(correyVotes) + ")")
    print(candidateList[2] + ": " + str(round(votePercentages[2])) + "%" + "(" + str(liVotes) + ")")
    print(candidateList[3] + ": " + str(round(votePercentages[3])) + "%"+ "(" + str(oTooleyVotes) + ")")
    print("---------------------")
    print("Winner: " + winner)
    print("---------------------")

printFinal()


# In[102]:


#print to text file
total_file = ("Election Results.txt")

with open(total_file,"w",) as file:
    file.write("Election Results")
    file.write("---------------------")
    file.write("Total Votes: " + str(totalVotes))
    file.write("---------------------")
    file.write(candidateList[0] + ": " + str(round(votePercentages[0])) + "%" + "(" + str(khanVotes) + ")")
    file.write(candidateList[1] + ": " + str(round(votePercentages[1])) + "%" + "(" + str(correyVotes) + ")")
    file.write(candidateList[2] + ": " + str(round(votePercentages[2])) + "%" + "(" + str(liVotes) + ")")
    file.write(candidateList[3] + ": " + str(round(votePercentages[3])) + "%"+ "(" + str(oTooleyVotes) + ")")
    file.write("---------------------")
    file.write("Winner: " + winner)
    file.write("---------------------")
        

    
total_file = ("Election Results.txt")


# In[ ]:




