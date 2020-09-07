#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# dependencies

df = []
df1 = []
election_csv = "Resources/election_data.csv"
election_df = pd.read_csv(election_csv)

# data = pd.read_csv (election_data.csv') 

df = pd.DataFrame(election_df, columns= ['Voter ID'])
totalNums = (len(df))
print("Total Votes: " + str(totalNums))

# list of candidate names who received votes

df1 = pd.DataFrame(election_df, columns= ['Candidate'])
name_arr = df1['Candidate'].values
can_name_list = list(dict.fromkeys(name_arr))
name_length = (len(can_name_list))
name_list = name_arr.tolist()
y_list = []

# determine vote count and percentage of votes for each candidate

def voteCount(name_list, x): 
    count = 0
    for ele in name_list: 
        if (ele == x): 
            count = count + 1
    return count  
for i in range(name_length):
    y = []
    x = can_name_list[i]
    y = name_list.count(can_name_list[i])
    z = round(y/totalNums * 100)
    print(x , ":" , z , "%" , "(" , y , ")")
    
# determine name of the winner

    for elem in name_list:
        if (elem == can_name_list[i]):
            y_list.append(y)
value_list = list(dict.fromkeys(y_list))
a = max(value_list)

if a == value_list[0]:
    print("Winner:", can_name_list[0], a)
elif a == value_list[1]:
    print("Winner:", can_name_list[1], a)
elif a == value_list[2]:
    print("Winner:", can_name_list[2], a)
else:
    print("Winner:", can_name_list[3], a)


    


# In[ ]:





# In[ ]:




