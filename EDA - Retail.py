#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df=pd.read_csv('SampleSuperstore.csv',sep=';')
df.head()


# ## Questions
# 1- Which shipment mode brings the most profits?
# 2- Which category sells the most quantities?
# 3- Which subcategory sold the most quantity?
# 4- Which region should we supply with more products?
# 5- Which region should we increase the publicity in to improve sales?
# 6- What is the most popular 5 orders?
# 7- Does the quantity of purchases get affected by the percentage of discount?

# In[22]:


print(df.isnull().sum())


# In[23]:


print(df.shape)
# Drop the 'county_name' and 'state' columns because it only contains missing values.
df.drop(['Segment', 'Postal Code'], axis='columns', inplace=True)
print(df.shape)


# In[24]:


df.dtypes


# In[26]:


df[['Ship Mode','Category','Region']]=df[['Ship Mode','Category','Region']].astype('category')


# In[27]:


df.info()


# In[28]:


df.describe()


# In[29]:


df.hist(figsize=(8,8));


# ### Which shipment mode brings the most profits?

# In[31]:


df.groupby('Ship Mode')['Profit'].sum().plot(kind='bar')


# ### Which category sells the most quantities?

# In[32]:


df.groupby('Category')['Quantity'].sum().plot(kind='bar')


# ### Which region should we supply with more products?

# In[45]:


df.groupby('Region')['Profit'].mean().sort_values(ascending=False).plot(kind='bar')


# ### Which region should we increase the publicity in to improve sales?

# In[50]:


df.groupby('Region')['Quantity'].sum().sort_values().plot(kind='pie',autopct='%.2f')


# Looks like the south buys the least number of products, so we should increase publicity there! 

# ### What is the most popular 5 orders?

# In[71]:


df2=df['Sub-Category'].value_counts(ascending=False)[:5]
df2.plot(kind='bar')
plt.xticks(rotation=90)
plt.show()


# ### Does the quantity of purchases get affected by the percentage of discount?

# In[80]:


dff=df['Discount'].sort_values()
dff


# In[83]:


df.groupby(dff)['Quantity'].count().plot(kind='bar')


# Looks like the most number of purchases happened at 20% discount and no discount, why is that?

# In[ ]:




