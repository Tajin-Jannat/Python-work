#!/usr/bin/env python
# coding: utf-8

# # Pandas Install

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd


# In[3]:


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)


# ## find specific row data

# In[4]:


print(myvar.loc[0])


# ## use of index

# In[6]:


df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)


# ## csv file import 

# In[8]:


df = pd.read_csv('data.csv')

print(df.to_string()) 


# In[ ]:




