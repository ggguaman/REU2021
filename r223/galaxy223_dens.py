#galaxy 223 gas density code with BH pos
import pynbody
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r223/cosmo25p.768sg1bwK1BHe75.007779')

#setting to physical units
s.physical_units()

#centering halo and aligning disk
pynbody.analysis.angmom.faceon(s)
#pynbody.analysis.angmom.sideon(s)

#creating gas density slice
sph.image(s.g,qty="rho",units="g cm^-3",width=20)

#plt.show()
plt.savefig("galaxy223_dens(side).png")
