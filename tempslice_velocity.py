#making pictures pynbody tutorial: tempurature slice from  velocity plot with BH position
import pynbody
import numpy as np
import pandas as pd
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt
from pynbody import filt, array

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cptmarvel.5.std')
s.physical_units()

#centering halo
pynbody.analysis.angmom.sideon(s)
s.rotate_x(90)

#creating temp slice with velocity plot
sph.image(s.g,qty="vr",vmin=-60,vmax=60,denoise=True,approximate_fast=False,log=False)

#function to find BH
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
print("The number of black holes is",len(BH))

#distance BH is from galaxy
with pynbody.analysis.halo.center(s, mode='hyb'):
    print([s],['pos'])

BHposition = BH['pos']
print("The black hole's position is",BH['pos'].in_units('kpc'))

#putting BH x in column
BHx=BHposition[[0],0]
print(BHx)

#putting BH y in column
BHy=BHposition[[0],1]
print(BHy)

#putting BH z in column
BHz=BHposition[[0],2]
print(BHy)

#plotting BH position
plt.plot(BHx,BHy, 'ro')

#plt.show()
plt.savefig("tempslice_velocity.png")
