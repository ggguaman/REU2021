#galaxy 204 GG Gas velocity code
import pynbody
import numpy as np
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r204/cosmo25p.768sg1bwK1BHe75.007779')

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
    
plt.show()
plt.savefig("galaxy204_GasVelGG.png")
