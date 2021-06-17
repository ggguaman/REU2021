#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pynbody


# In[4]:


#loading high redshift
f1 = pynbody.load("/Users/mac/Desktop/tutorial_gadget/snapshot_018")


# In[5]:


#loading low redshift
f2 = pynbody.load("/Users/mac/Desktop/tutorial_gadget/snapshot_020")


# In[6]:


#verifying redshifts
"f1 redshift=%.2f; f2 redshift=%.2f"%(f1.properties['z'], f2.properties['z'])


# In[7]:


#loading halo at low redshift
h2 = f2.halos()


# In[8]:


#creating bridge between f1 and f2
b = f2.bridge(f1)


# In[9]:


#looking where halo 9 particles from low redshift came from in high redshift
progenitor_particles = b(h2[9]) #contains halo 9 particles from high redshift


# In[10]:


#verifying
h2[9]['iord']


# In[11]:


#verifying
progenitor_particles['iord']


# In[12]:


#verifying
all(h2[9]['iord'] == progenitor_particles['iord'])


# In[13]:


progenitor_particles['x']


# In[14]:


h2[9]['x']


# In[15]:


#Identifying halos between different outputs
cat = b.match_catalog()


# In[16]:


cat


# In[ ]:




