#gas tempurature plot with BHs pos
import pynbody
import numpy as np
from matplotlib import colors
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cosmo25p.768sg1bwK1BHe75.008192')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.faceon(s)
#pynbody.analysis.angmom.sideon(s)

#creating slice to show gas temp
sph.image(s.g,qty="temp",width=40,denoise=True,approximate_fast=False,log=True)

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
print("The BHs position is: ",BH['pos'].in_units('kpc'))

for i in range(len(BH)):
    BHx=BHposition[[i],0]
    BHy=BHposition[[i],1]
    BHz=BHposition[[i],2]
    plt.plot(BHx,BHy, 'ro')
    #sphere filter
    radius = "2 kpc"
    centre = (BHx[0], BHy[0], BHz[0])
    sphere = s.g[pynbody.filt.Sphere(radius, centre)]
    print("The number of particles in the sphere is: ",len(sphere))
    print("The BHs temperature is ",sphere["temp"])
    print("The average temperature is: ",sphere["temp"].mean())

plt.show()
#plt.savefig("galaxy109_temp.png")
#plt.savefig("galaxy109_temp(side).png")
