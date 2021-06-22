#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pynbody
import matplotlib.pylab as plt


# In[2]:


#loading snapshot
s = pynbody.load('/Users/mac/Desktop/testdata/g15784.lr.01024.gz')


# In[3]:


s.physical_units()


# In[4]:


#loading halo catalogue
h = s.halos()


# In[5]:


#total numbers of halos in catalogue
len(h)


# In[6]:


#total numbers of particles in halos 1 and 2
len(h[1]), len(h[2])


# In[7]:


#halo 1 total mass
h[1]['mass'].sum().in_units('1e12 Msol')


# In[8]:


#position of particles
h[1]['pos'][:5]


# In[9]:


#centering halo
pynbody.analysis.halo.center(h[1])


# In[10]:


im = pynbody.plot.image(h[1].d, width = '500 kpc', cmap=plt.cm.Greys, units = 'Msol kpc^-2')


# In[11]:


#using properties to see sub-halos
h[1].properties['children']


# In[12]:


#using keys to see properties of halo
h[1].properties.keys()


# In[13]:


#big simulations and lots of halos
f = pynbody.load("/Users/mac/Desktop/testdata/g15784.lr.01024")


# In[14]:


#not loading file but accessing catalogue
h = f.halos()


# In[15]:


#property calculated by Amiga Halo Finder in Msol/h
h[2].properties['mass']/1e12 


# In[16]:


len(h[2])


# In[17]:


#loading only properties dictionary
h = f.halos(dummy=True)


# In[18]:


h[2].properties['mass']


# In[19]:


len(h[2])


# In[20]:


#using partial-loading system to only pull a single halo into the computer’s memory at once
h2data = h.load_copy(2)


# In[21]:


len(h2data)


# In[22]:


h2data['mass']


# In[23]:


#using SubFind: halo catalogue is a separate file to the snapshot
s = pynbody.load('/Users/mac/Desktop/testdata/Test_NOSN_NOZCOOL_L010N0128/data/snapshot_103/snap_103.hdf5')


# In[24]:


s.physical_units()


# In[25]:


#accessing subfind output directly
s = pynbody.load('/Users/mac/Desktop/testdata/Test_NOSN_NOZCOOL_L010N0128/data/subhalos_103/subhalo_103')


# In[26]:


s.physical_units()


# In[27]:


#h is the Friends-of-Friends(FOF) catalogue
h = s.halos()


# In[28]:


#retrieving total number of halos
len(h), h.ngroups, h.nsubhalos


# In[29]:


#returns the number of particles in halos 1 and 2
len(h[1]), len(h[2])


# In[30]:


#total mass in the second FOF halo
h[1]['mass'].sum().in_units('1e12 Msol')


# In[31]:


#position of its first few particles
h[1]['pos'][:5]


# In[32]:


#centering simulation on halo
pynbody.analysis.halo.center(h[1], vel=False)


# In[33]:


im = pynbody.plot.image(h[1].d, width = '40 kpc', cmap=plt.cm.Greys, units = 'Msol kpc^-2')


# In[34]:


#accessing list of subhalos
h[1].sub[:]


# In[35]:


h[1].sub[0].d['vel']


# In[36]:


#subhalo properties list is more extensive than FOF halo
h[2].properties


# In[37]:


h[2].properties['CenterOfMass']


# In[38]:


h[2].sub[4].properties


# In[39]:


#accessing entire dataset of property requires embedded for loop over HDF5 catalogue and appending to an array
SubStellarVelDisp = [[subhalo.properties['SubStellarVelDisp'] for subhalo in halo.sub] for halo in h]


# In[40]:


SubStellarVelDisp[5]


# In[ ]:




