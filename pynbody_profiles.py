#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pynbody
from pynbody.analysis import profile
import matplotlib.pylab as plt


# In[2]:


#loading snapshot
s = pynbody.load('/Users/mac/Desktop/testdata/g15784.lr.01024') 
s.physical_units()


# In[3]:


#loading halos
h = s.halos()


# In[4]:


#centering on largest halo and aligning disk
pynbody.analysis.angmom.faceon(h[1])


# In[5]:


#making profile
p = profile.Profile(h[1].s, rmin='.01 kpc', rmax='50 kpc')


# In[6]:


pdm_sph = profile.Profile(s.d, rmin = '.01 kpc', rmax = '250 kpc')


# In[7]:


#checking available profiles
p.derivable_keys()


# In[8]:


#plotting a metallicity(feh) profile
plt.plot(p['rbins'].in_units('kpc'),p['feh'],'k')
#plot labels
plt.xlabel('$R$ [kpc]') 
plt.ylabel('[Fe/H]')


# In[9]:


#automatically creating derivatives of profiles
p_all = profile.Profile(s, rmin='.01 kpc', rmax='250 kpc')


# In[10]:


#returning potential profile
p_all['pot'][0:10] 


# In[11]:


#returning d phi / dr from p["phi"]
p_all['d_pot'][0:10] 


# In[12]:


#calculating dispersions and root-mean-square values to get stellar velocity dispersion
plt.clf(); plt.plot(p['rbins'].in_units('kpc'),p['vr_disp'].in_units('km s^-1'),'k')
#labels
plt.xlabel('$R$ [kpc]') 
plt.ylabel('$\sigma_{r}$')


# In[13]:


#making quantile profile that can return any quantile range
p_quant = profile.QuantileProfile(h[1].s, rmin = '0.1 kpc', rmax = '50 kpc')


# In[14]:


plt.clf() 
plt.plot(p_quant['rbins'], p_quant['feh'][:,1], 'k')
plt.fill_between(p_quant['rbins'], p_quant['feh'][:,0], p_quant['feh'][:,2], color = 'Grey', alpha=0.5)
#labels
plt.xlabel('$R$ [kpc]') 
plt.ylabel('[Fe/H]')


# In[15]:


#makeing profile of stars in halo 1 according to age
s.s['age'].convert_units('Gyr')


# In[16]:


p_age = profile.Profile(h[1].s, calc_x = lambda x: x.s['age'], rmax = '10 Gyr')


# In[17]:


#plotting
plt.clf() 
plt.plot(p_age['rbins'], p_age['feh'], 'k', label = 'mean [Fe/H]')


# In[18]:


#customizing plot line
plt.plot(p_age['rbins'], p_age['feh_disp'], 'k--', label = 'dispersion')
#labels
plt.xlabel('Age [Gyr]') 
plt.ylabel('[Fe/H]')
plt.legend()


# In[19]:


#creating vertical profile to analyze disk structure
p_vert = profile.VerticalProfile(h[1].s, '3 kpc', '5 kpc', '5 kpc')


# In[20]:


#specifying radial range and max z
plt.clf() 
plt.plot(p_vert['rbins'].in_units('pc'), p_vert['density'].in_units('Msol pc^-3'),'k')
#labels
plt.xlabel('$z$ [pc]') 
plt.ylabel(r'$\rho_{\star}$ [M$_{\odot}$ pc$^{-3}$]')


# In[21]:


#rotating the snapshot by 60 degrees to make inclined profile
s.rotate_x(60) 


# In[22]:


p_inc = profile.InclinedProfile(h[1].s, 60, rmin = '0.1 kpc', rmax = '50 kpc')


# In[ ]:




