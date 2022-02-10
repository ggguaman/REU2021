#galaxy 239 gas density code with BH pos
import pynbody
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r239/cosmo25p.768sg1bwK1BHe75.007779')

#setting to physical units
s.physical_units()

#centering halo and aligning disk
pynbody.analysis.angmom.faceon(s)
#pynbody.analysis.angmom.sideon(s)

#creating gas density slice
sph.image(s.g,qty="rho",units="g cm^-3",width=20)

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
print("The black hole's position is", BH['pos'].in_units('kpc'))

#putting BH x in column
BHx=BHposition[[0],0]
#print(BHx)

#putting BH y in column
BHy=BHposition[[0],1]
#print(BHy)

#putting BH z in column
BHz=BHposition[[0],2]
#print(BHz)

#plotting BH position
plt.plot(BHx,BHy, 'ro')

radius = "1 kpc"
centre = (BHx[0], BHy[0], BHz[0])
sphere = s[pynbody.filt.Sphere(radius,centre)]
print(sphere["mass"].sum())
    
plt.show()
#plt.savefig("galaxy239_dens.png")
#plt.savefig("galaxy239_dens(side).png")
