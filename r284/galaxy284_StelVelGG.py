#galaxy 284 GG Stellar velocity code
import pynbody
import numpy as np
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r284/cosmo25p.768sg1bwK1BHe75.007779')
#s=pynbody.load('/mnt/data0/jillian/gguaman/r284/r284.007779.tipsy')

#setting to physical units
s.physical_units()

#centering halo
#pynbody.analysis.angmom.faceon(s)
pynbody.analysis.angmom.sideon(s)

#creating star velocity plot
sph.image(s.s,qty="vz",width='30 kpc',cmap="PuOr", log=False, units='km s**-1')

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

#plt.show()
plt.savefig("galaxy284_StelVelGG.png")
