#galaxy 109 ionized gas code with BHs pos
import pynbody
import numpy as np
import pandas as pd
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt
from pynbody import filt, array

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cosmo25p.768sg1bwK1BHe75.008192')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.faceon(s)
#pynbody.analysis.angmom.sideon(s)

#filter to only use ionised gas
GasFilter = pynbody.filt.HighPass('temp','15848 K')

#creating image to show velocity of ionised gas
sph.image(s.g[GasFilter],qty="vr",vmin=-20,width=40,denoise=True,approximate_fast=False,log=False)

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
#print("The black hole's position is", BHposition)
print("The BHs position is",BH['pos'].in_units('kpc'))

for i in range(len(BH)):
    BHx=BHposition[[i],0]
    BHy=BHposition[[i],1]
    BHz=BHposition[[i],2]
    plt.plot(BHx,BHy, 'ro')
    #filter sphere
    radius = "2 kpc"
    centre = (BHx[0], BHy[0], BHz[0])
    #print(centre)
    sphere = s.g[GasFilter][pynbody.filt.Sphere(radius, centre)]
    print("The number of particles in the sphere is: ",len(sphere))
    print("The BHs density is", sphere["rho"])
    print("The average density is: ",sphere["rho"].mean())
    
plt.show()
#plt.savefig("galaxy109_iongas.png")
#plt.savefig("galaxy109_iongas(side).png")
