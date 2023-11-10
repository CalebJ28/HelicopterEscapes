#!/usr/bin/env python
# coding: utf-8

# # Analyzing Data

# ## Prison Helicopter Escapes

# We begin by importing some helper functions.

# In[83]:


from helper import *


# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[84]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'
data = data_from_url(url)


# Let's print the first three rows

# In[85]:


index = 0
for row in data:
    data[index] = row[:-1] 
    index += 1
print(data[3:])


# In[87]:


for row in data:
        row[0] = fetch_year(row[0])
print(data[3:])


# In[88]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]

years = []
for year in range(min_year, max_year + 1):
    years.append(year)


# In[91]:


attempts_per_year = []
for year in years:
    attempts_per_year.append([year,0])
    
print(attempts_per_year[:30])


# In[96]:


# Instruction 1 - for each row in data
for row in data:
    
    for year_attempt in attempts_per_year: # Instruction 2 - nothing to do here
        
        # Instruction 3 - assign the year value in year_attempt to year
        year = year_attempt[0]
        
        if row[0] == year:
            year_attempt[1] += 1

# Instruction 4 - print the results
print(attempts_per_year)


# In[97]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# In which year did the most attempts at breaking out of prison with a helicopter occur?

# In[ ]:




