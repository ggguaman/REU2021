#!/usr/bin/env python
# coding: utf-8

# In[1]:


#loading test files
import pynbody
import numpy as np
#f known as SimSnap(inspects path and decides the file format)
f = pynbody.load("/Users/mac/Desktop/testdata/test_g2_snap")


# In[2]:


#searching number of particles in file
len(f)


# In[3]:


#searching specific particle 'types'(families)
f.families()


# In[4]:


#searching number of each specific particle
len(f.dm)


# In[5]:


#searching number of each specific particle
len(f.gas)


# In[6]:


#searching number of each specific particle
len(f.star)


# In[7]:


#file info stored in properties dictionary
f.properties


# In[8]:


#accessing property a from dictionary
f.properties['a']


# In[9]:


#array dictionary
f.keys()


# In[10]:


#what could be loaded from keys(array dict.)
f.loadable_keys()


# In[11]:


#3D coordinatiates of all properties array
f['pos']


# In[12]:


#arrays available for gas family
f.gas.loadable_keys()


# In[13]:


#density of gas particles
f.gas['rho']


# In[14]:


#creating own array
f['twicethemass'] = f['mass']*2


# In[15]:


#array for only one family
f.gas['myarray'] = f.gas['rho']**2


# In[16]:


#derived arrays that are [re]calculated on demand
@pynbody.derived_array
def thricethemass(sim) :
    return sim['mass']*3


# In[17]:


#when calling array values are calculated and stored
f['thricethemass']


# In[18]:


#changing mass array
f['mass'][0] = 1


# In[19]:


#recalculates and changes thrice array
f['thricethemass']


# In[20]:


#printing units of array
f['mass'].units


# In[21]:


#converting array to correct units
f['pos'].in_units('Mpc')


# In[22]:


#requesting pynbody change array to something sensible
f.physical_units()


# In[23]:


f.gas['rho']


# In[24]:


#future arrays will also be converted
f['vel']


# In[25]:


#new generated array will have correct units
5*f['vel']


# In[26]:


(f['vel']**2).units


# In[27]:


np.sqrt(((f['vel']**2).sum(axis=1)*f['mass'])).units


# In[28]:


#converting numpy array to pynbody array
array = pynbody.array.SimArray(np.random.rand(10))


# In[29]:


#linking array to simulation
array.sim = f


# In[30]:


#units that require cosmology info
array.units = 'Mpc a'


# In[31]:


array


# In[32]:


array.in_units('kpc')


# In[33]:


#slicing to get every 10th particle
every_tenth = f[::10]


# In[34]:


#display length
len(every_tenth)


# In[35]:


#changing position of particle
every_tenth['pos'][1]


# In[36]:


#changing position of particle
every_tenth['pos'][1] = [1,2,3]


# In[37]:


#changing position of particle
every_tenth['pos'][1]


# In[38]:


#can see change in main snapshot
f['pos'][10]


# In[41]:


#passing boolean array to determine if particle should be included(true) or not(false)
f_slab = f[(f['x']>1000)&(f['x']<2000)]


# In[42]:


#f_slab only pointing at particles that have x-coordinates between 1000 and 2000.
f_slab['x'].min()


# In[43]:


f_slab['x'].max()


# In[44]:


f['x'].min()


# In[45]:


f['x'].max()


# In[46]:


#returning length of slab
len(f_slab.dm)


# In[47]:


#returning length of subsnap of slab
len(f_slab.dm[::10])


# In[48]:


f_slab[[100,105,252]].gas['pos']


# In[49]:


#importing filter from pynbody
from pynbody.filt import *


# In[50]:


#using a filter to pick out a sphere centered on the origin
f_sphere = f[Sphere('10 kpc')]


# In[ ]:




