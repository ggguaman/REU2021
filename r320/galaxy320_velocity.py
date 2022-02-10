#galaxy 320 gas velocity code with BH pos
import pynbody
import numpy as np
import pandas as pd
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r320/cosmo25p.768sg1bwK1BHe75.007779')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.faceon(s)
#pynbody.analysis.angmom.sideon(s)

#creating gas velocity plot
sph.image(s.g,qty="vr",width=20,denoise=True,approximate_fast=False,log=False)

#function to find BH
def findBH(s):
    BHfilter=pynbody.filt.LowPass('tform',0.0)
    BH=s.stars[BHfilter]
    return BH
BH=findBH(s)
print("The number of black holes is",len(BH))

#distance BH is from galaxy
#with pynbody.analysis.halo.center(s, mode='hyb'):
#print([s],['pos'])

BHposition = BH['pos']
#print("The black hole's postion is", BHposition)
print("The BHs position is ",BH['pos'].in_units('kpc'))

for i in range(len(BH)):
    #putting BH x in column
    BHx=BHposition[[i],0]
    #putting BH y in column
    BHy=BHposition[[i],1]
    #putting BH z in column
    BHz=BHposition[[i],2]
    plt.plot(BHx,BHy, 'ro')
    #sphere filter
    radius = "1.25 kpc"
    center = (BHx[0], BHy[0], BHz[0])
    sphere = s.g[pynbody.filt.Sphere(radius, center)]
    print("The number of particles in the sphere is: ",len(sphere))
    print("The velocity is ",sphere["vr"])
    print("The average velocity is: ",sphere["vr"].mean())
    
plt.show()
#plt.savefig("galaxy320_velocity.png")
#plt.savefig("galaxy320_velocity(side).png")
