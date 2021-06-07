#!/usr/bin/env python
# coding: utf-8

# first plot assignment: redshift v time

# In[26]:


import numpy as np
import matplotlib.pyplot as plt
#x,y=np.loadtxt("times.txt",float,unpack=True)
#f = open("/Users/mac/Desktop/REU2021/times.list", "r")
         #D:\\Users\mac\Desktop\REU2021\times.list", "r")
#print(f.read())

#loading data from file to code
x,y=np.loadtxt("/Users/mac/Desktop/REU2021/times.list", unpack=True)

#setting the size of plot
plt.figure(figsize=([14,5]))

#creating scatter plot of data
plt.scatter(x,y)

#labels for plot
plt.title('Time vs. Red Shift')
plt.xlabel('Time (Gyr)')
plt.ylabel('Redshift')


# In[ ]:




