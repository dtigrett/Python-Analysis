#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Dependencies
import pandas as pd


# In[6]:


# save file path to variable
budget_csv = "Resources/budget_data.csv"


# In[7]:


# read with pandas
budget_df = pd.read_csv(budget_csv)
budget_df.head()


# In[10]:


#The total number of months included in the dataset
len(budget_df)


# In[11]:


# The net total amount of "Profit/Losses" over the entire period
budget_df["Profit/Losses"].sum()


# In[18]:


#The average of the changes in "Profit/Losses" over the entire period
differences=[]
previous = 0
for index,row in budget_df.iterrows():
   # print(row["Profit/Losses"])
    change = row["Profit/Losses"] - previous
    previous = row["Profit/Losses"]
    if index >0:
        differences.append(change)
average = sum(differences)/len(differences)
average


# In[19]:


# The greatest increase in profits (date and amount) over the entire period
max(differences)


# In[20]:


# The greatest decrease in losses (date and amount) over the entire period
min(differences)


# In[ ]:




