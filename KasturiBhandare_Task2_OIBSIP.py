#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[17]:


data = pd.read_csv(r'C:\Users\Kasturi\Downloads\umployment\Unemployment in India.csv')
data


# # Evaluating the missing values

# In[18]:


print(data.isnull().sum())


# In[19]:


data.columns= ["Region","Date","Frequency","Estimated Unemployment Rate","Estimated Employed",
               "Estimated Labour Participation Rate","Area"]


# In[20]:


plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12, 10))


# In[21]:


sns.heatmap(data.corr())
plt.show()


# # Visualizing the data

# In[22]:


data.columns= ["Region","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Area"]


# In[27]:


plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region", data=data)
plt.show()


# In[28]:


plt.figure(figsize=(12, 10))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate", hue="Area", data=data)
plt.show()


# In[ ]:




