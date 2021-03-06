#galaxy 320 ionized gas code with BHs pos
import pynbody
import numpy as np
import pandas as pd
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt
from pynbody import filt, array

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r320/cosmo25p.768sg1bwK1BHe75.007779')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.faceon(s)
#pynbody.analysis.angmom.sideon(s)

#filter to only use ionised gas
GasFilter = pynbody.filt.HighPass('temp','15848 K')

#creating image to show velocity of ionised gas
sph.image(s.g[GasFilter],qty="vr",vmin=-20,width=20,denoise=True,approximate_fast=False,log=False)

#function to find BH
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
print("The number of black holes is",len(BH))

#distance BH is from galaxy
#with pynbody.analysis.halo.center(s, mode='hyb'):
#print([s],['pos'])

BHposition = BH['pos']
print("The black hole's position is", BHposition)

for i in range(len(BH)):
    BHx=BHposition[[i],0]
    BHy=BHposition[[i],1]
    BHz=BHposition[[i],2]
    plt.plot(BHx,BHy, 'ro')
    #sphere filter
    radius = "1.25 kpc"
    center = (BHx[0], BHy[0], BHz[0])
    sphere = s.g[GasFilter][pynbody.filt.Sphere(radius, center)]
    print("The number of particles in the sphere is: ",len(sphere))
    print("The density is ",sphere["rho"])
    print("The average density is: ",sphere["rho"].mean())
    
plt.show()
#plt.savefig("galaxy320_iongas.png")
#plt.savefig("galaxy320_iongas(side).png")
