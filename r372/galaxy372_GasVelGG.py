#galaxy 372 GG Gas velocity code
import pynbody
import numpy as np
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r372/cosmo25p.768sg1bwK1BHe75.007779')
#s=pynbody.load('/mnt/data0/jillian/gguaman/r372/r372.007779.tipsy')

#setting to physical units
s.physical_units()

#centering halo
#pynbody.analysis.angmom.faceon(s)
pynbody.analysis.angmom.sideon(s)

#creating star velocity plot
sph.image(s.g,qty="vz",width='20 kpc',cmap="RdBu", log=False, units='km s**-1')

#function to find BH
def findBH(s):
    BHfilter=pynbody.filt.LowPass('tform',0.0)
    BH=s.stars[BHfilter]
    return BH
BH=findBH(s)
print("The number of black holes is:",len(BH))
   
#plt.show()
plt.savefig("galaxy372_GasVelGG.png")
