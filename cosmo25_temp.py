#gas tempurature plot
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

#creating slice to show gas temp
sph.image(s.g,qty="temp",width=30,denoise=True,approximate_fast=False,log=True)

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
print("The black hole's postion is", BHposition)
#print(BH['pos'].in_units('kpc'))

for i in range(len(BH)):
    BHx=BHposition[[i],0]
    BHy=BHposition[[i],1]
    BHz=BHposition[[i],2]
    plt.plot(BHx,BHy, 'ro')

#plt.show()
plt.savefig("cosmo25_temp.png")
