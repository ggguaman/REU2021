#galaxy 320 GG Stellar velocity map
import pynbody
import numpy as np
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
#s=pynbody.load('/mnt/data0/jillian/gguaman/r320/cosmo25p.768sg1bwK1BHe75.007779')
s=pynbody.load('/mnt/data0/jillian/gguaman/r320/r320.007779.tipsy')
#setting to physical units
s.physical_units()

#centering halo
#pynbody.analysis.angmom.faceon(s)
pynbody.analysis.angmom.sideon(s)

#creating star velocity plot
sph.image(s.s,qty="vz",av_z="mass",width='20 kpc',cmap="PuOr", log=False, units='km s**-1')

#function to find BH
def findBH(s):
    BHfilter=pynbody.filt.LowPass('tform',0.0)
    BH=s.stars[BHfilter]
    return BH
BH=findBH(s)
print("The number of black holes is:",len(BH))

BHposition = BH['pos']
#print("The black hole's postion is", BHposition)
print("The BHs position is",BH['pos'].in_units('kpc'))

for i in range(len(BH)):
    #putting BH x in column
    BHx=BHposition[[i],0]
   #putting BH y in column
    BHy=BHposition[[i],1]
   #putting BH z in column
    BHz=BHposition[[i],2]
    plt.plot(BHx,BHy, 'ro')
    #sphere filter
    #radius = "1.25 kpc"
    #center = (BHx[0], BHy[0], BHz[0])
    #sphere = s.g[pynbody.filt.Sphere(radius, center)]
    #print("The number of particles in the sphere is:",len(sphere))
    #print("The stellar velocity is",sphere["vel"])
    #print("The average stellar velocity is:",sphere["vel"].mean())
    
plt.show()
#plt.savefig("galaxy320_StelVel.png")
#plt.savefig("galaxy320_StelVel(side).png")
#plt.savefig("galaxy320_StelVel(z_side).png")
