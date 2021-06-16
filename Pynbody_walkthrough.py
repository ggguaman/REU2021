#!/usr/bin/env python
# coding: utf-8

# In[1]:


#loading data
import pynbody
import pylab
s=pynbody.load('/Users/mac/Desktop/testdata/g15784.lr.01024.gz')


# In[2]:


#loading halos
h=s.halos()


# In[3]:


#storing halo
h1=h[1]


# In[4]:


#checking number of particles in each type
print('ngas = %e, ndark = %e, nstar = %e\n'%(len(h1.gas),len(h1.dark),len(h1.star)))


# In[5]:


#centering data
pynbody.analysis.halo.center(h1,mode='hyb')


# In[6]:


#centering contents of halo 5
print(h[1]['pos'][0])


# In[7]:


#centering contents of halo 5
print(h[5]['pos'][0])


# In[8]:


#centering contents of halo 5
h5=h[5]


# In[9]:


#centering contents of halo 5
my_h5_transform = pynbody.analysis.halo.center(h5, mode='hyb', move_all=False)


# In[10]:


#centering contents of halo 5
print(h[1]['pos'][0]) #unchanged as before


# In[11]:


#centering contents of halo 5
print(h5['pos'][0]) #changed as before


# In[12]:


#transformation that allows undo
my_h5_transform.revert()


# In[13]:


#reverted to original
print(h5['pos'][0])


# In[14]:


#still same as before
print(h[1]['pos'][0])


# In[15]:


#more effective way to transform
with pynbody.analysis.halo.center(h[5], mode='hyb'): print(h[5]['pos'][0])


# In[16]:


#reverts like before
print(h[5]['pos'][0])


# In[17]:


#making sure center coordinates pynbody finds are reasonable
s = pynbody.load('/Users/mac/Desktop/testdata/g15784.lr.01024.gz'); h1 = s.halos()[1];
cen_hyb = pynbody.analysis.halo.center(h1,mode='hyb',retcen=True)
cen_pot = pynbody.analysis.halo.center(h1,mode='pot',retcen=True)
print(cen_hyb)


# In[18]:


#making sure center coordinates pynbody finds are reasonable
print(cen_pot)


# In[19]:


#cen_hyb was better so keeping it
s['pos'] -= cen_hyb


# In[20]:


#converting to physical units
s.physical_units()


# In[21]:


#display plot
pynbody.plot.image(h1.g, width=100, cmap='Blues')


# In[22]:


#larger scale dark matter distribution
pynbody.plot.image(s.d[pynbody.filt.Sphere('10 Mpc')], width='10 Mpc', units = 'Msol kpc^-2', cmap='Greys');


# In[23]:


#aligning edge-on
pynbody.analysis.angmom.sideon(h1, cen=(0,0,0))
pynbody.plot.image(h1.g, width=100, cmap='Blues');


# In[24]:


#rotating face-on
s.rotate_x(90)


# In[32]:


#star profile using face-on orientation
ps = pynbody.analysis.profile.Profile(h1.s, min = 0.01, max = 50, type = 'log')
pylab.clf()
pylab.plot(ps['rbins'], ps['density']);
pylab.semilogy();
pylab.xlabel('$R$ [kpc]');
pylab.ylabel('$\Sigma$ [M$_\odot$/kpc$^2$]');


# In[33]:


#generating rotation curve profile
pylab.figure()


# In[34]:


pd = pynbody.analysis.profile.Profile(h1.d,min=.01,max=50, type = 'log')


# In[35]:


pg = pynbody.analysis.profile.Profile(h1.g,min=.01,max=50, type = 'log')


# In[36]:


p = pynbody.analysis.profile.Profile(h1,min=.01,max=50, type = 'log')


# In[43]:


for prof, name in zip([p,pd,ps,pg],['total','dm','stars','gas']) : pylab.plot(prof['rbins'],prof['v_circ'],label=name)
pylab.xlabel('$R$ [kpc]');
pylab.ylabel('$v_{circ}$ [km/s]');


# In[ ]:




