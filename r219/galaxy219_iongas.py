#galaxy 219 ionized gas with BH pos
import pynbody
import numpy as np
import pandas as pd
import pynbody.plot.sph	as sph
import matplotlib.pyplot as plt
from pynbody import filt, array

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r219/cosmo25p.768sg1bwK1BHe75.007779')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.faceon(s)

#filter to only use ionised gas
GasFilter = pynbody.filt.HighPass('temp','15848 K')

#creating image to show velocity of ionised gas
sph.image(s.g[GasFilter],qty="vr",vmin=-20,width=40,denoise=True,approximate_fast=False,log=False)

#function to find BH
def findBH(s):
    BHfilter=pynbody.filt.LowPass('tform',0.0)
    BH=s.stars[BHfilter]
    return BH
BH=findBH(s)
print("The number of black holes is",len(BH))

#distance BH is from galaxy
#with pynbody.analysis.halo.center(s, mode='hyb'):
print([s],['pos'])

BHposition = BH['pos']
print("The black hole's position is", BH['pos'].in_units('kpc'))

#putting BH x in column
BHx=BHposition[[0],0]
#print(BHx)

#putting BH y in column
BHy=BHposition[[0],1]
#print(BHy)

#putting BH z in column
BHz=BHposition[[0],2]
#print(BHz)

#plotting BH position
plt.plot(BHx,BHy, 'ro')

#plt.show()
plt.savefig("galaxy219_iongas.png")
