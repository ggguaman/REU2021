#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#using a slice of an existing numpy array
a = np.zeros(10)


# In[3]:


b = a[3:5]


# In[4]:


b[1] = 100


# In[5]:


#changing b updated a
a


# In[6]:


#indexing a numpy array
c = a[[4,5,6]]


# In[7]:


c[1] = 200


# In[8]:


#changing c doesn't update a because c copied the relevant data instead of pointing back at it
a


# In[10]:


import pynbody


# In[11]:


#IndexedSubArray class fixes this problem
d = pynbody.array.IndexedSimArray(a, [4,5,6])


# In[12]:


d[1] = 200


# In[13]:


#a has been updated because the IndexedSimArray emulates rather than wrapping a numpy array
a


# In[14]:


#every time you call a function that requires a numpy array as an input, the IndexedSimArray has to generate a proxy 
get_ipython().run_line_magic('time', 'for i in range(10000) : d+=1')


# In[15]:


get_ipython().run_line_magic('time', 'for i in range(10000) : a+=1')


# In[16]:


#how to avoid constructing IndexedSimArray`s and force only numpy arrays to be returned(immediate mode)
f = pynbody.new(dm=100) #test snapshot


# In[17]:


#subview into test snapshot
sub_f = f[[20,21,22]]


# In[19]:


sub_mass = sub_f['mass']


# In[20]:


type(sub_mass)


# In[21]:


sub_mass[:]=3


# In[22]:


f['mass'][[20,21,22]]


# In[24]:


#immediate mode: updating returned numpy array has no effect on snapshot
with f.immediate_mode:
    sub_mass = sub_f['mass']


# In[25]:


type(sub_mass)


# In[26]:


sub_mass


# In[27]:


sub_mass[:]=5


# In[28]:


#updated
sub_mass


# In[29]:


#not updated
f['mass'][[20,21,22]]


# In[ ]:




