#r109 gas density plot with BHs pos
import pynbody
import numpy as np
from pynbody.filt import *
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cosmo25p.768sg1bwK1BHe75.008192')

#setting to physical units
s.physical_units()

#centering halo and aligning disk
pynbody.analysis.angmom.faceon(s)
#pynbody.analysis.angmom.sideon(s)

#creating gas density slice
sph.image(s.g,qty="rho",units="g cm^-3",width=40)

#function to find BH
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
print("The number of black holes is",len(BH))

#distance BH is from galaxy
#with pynbody.analysis.halo.center(s, mode='hyb'):
print([s],['pos'])

BHposition = BH['pos']
print("The black hole's position is", BHposition)

for i in range(len(BH)):
    BHx=BHposition[[i],0]
    BHy=BHposition[[i],1]
    BHz=BHposition[[i],2]
    plt.plot(BHx,BHy,'ro')
    radius = "1 kpc"
    centre = (BHx[0], BHy[0], BHz[0])
    #print(centre)
    sphere = s[pynbody.filt.Sphere(radius, centre)]
    print(sphere["rho"].sum())
    
plt.show()
#plt.savefig("galaxy109_dens.png")
#plt.savefig("galaxy109_dens(side).png")
