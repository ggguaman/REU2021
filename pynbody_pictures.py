#!/usr/bin/env python
# coding: utf-8

# Density Slice

# In[12]:


import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt

#loading snapshot
s = pynbody.load('/Users/mac/Desktop/testdata/g15784.lr.01024.gz')

#setting to physical units
s.physical_units()

#loading halos
h = s.halos()

#centering on the largest halo and aligning the disk
pynbody.analysis.angmom.faceon(h[1])

#creating a slice of gas density
sph.image(h[1].g,qty="rho",units="g cm^-3",width=100,cmap="Greys")


# Integrated Density

# In[14]:


import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt

#loading snapshot 
s = pynbody.load('/Users/mac/Desktop/testdata/g15784.lr.01024.gz')
#setting to physical units
s.physical_units()

#loading the halos
h = s.halos()

#centering on the largest halo and aligning the disk
pynbody.analysis.angmom.faceon(h[1])
#creating an image of gas density integrated down the line of site (z axis)
sph.image(h[1].g,qty="rho",units="g cm^-2",width=100,cmap="Greys")


# Temperature Slice

# In[15]:


import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt

#loading the snapshot
s = pynbody.load('/Users/mac/Desktop/testdata/g15784.lr.01024.gz')
#setting to physical units
s.physical_units()

#loading the halos
h = s.halos()

#centering on the largest halo and aligning the disk
pynbody.analysis.angmom.sideon(h[1])
#creating a slice showing the gas temperature
sph.image(h[1].g,qty="temp",width=50,cmap="YlOrRd", denoise=True,approximate_fast=False)


# Velocity Vectors

# In[17]:


import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt

#loading the snapshot
s = pynbody.load('/Users/mac/Desktop/testdata/g15784.lr.01024.gz')
#setting to physical units
s.physical_units()

#loading the halos
h = s.halos()

#centering on the largest halo and aligning the disk
pynbody.analysis.angmom.sideon(h[1])

#creating subplots
f, axs = plt.subplots(1,2,figsize=(14,6))

#creating a slice showing the gas temperature, with velocity vectors overlaid
sph.velocity_image(h[1].g, vector_color="cyan", qty="temp",width=50,cmap="YlOrRd",denoise=True,approximate_fast=False, subplot=axs[0], show_cbar = False)

#can also make a stream visualization instead of a quiver plot
pynbody.analysis.angmom.faceon(h[1])
s['pos'].convert_units('Mpc')
sph.velocity_image(s.g, width='3 Mpc', cmap = "Greys_r", mode='stream', units='Msol kpc^-2', 
                   density = 2.0, vector_resolution=100, vmin=1e-1,subplot=axs[1], 
                   show_cbar=False, vector_color='black')


# Multi-band Images of Stars

# In[11]:


import pynbody
import matplotlib.pylab as plt

# load the snapshot and set to physical units
s = pynbody.load('/Users/mac/Desktop/testdata/g15784.lr.01024.gz')
s.physical_units()

# load the halos
h = s.halos()

# center on the largest halo and align the disk
pynbody.analysis.angmom.sideon(h[1])
#creating an image using the default bands (i, v, u)
pynbody.plot.stars.render(s,width='20 kpc')


# In[ ]:




