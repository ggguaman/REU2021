#gas tempurature plot
import pynbody
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cosmo25p.768sg1bwK1BHe75.008192')

#setting to physical units
s.physical_units()

#centering halo and aligning disk
pynbody.analysis.angmom.faceon(s)

#creating gas density slice
sph.image(s.g,qty="rho",units="g cm^-3",width=10)

plt.show()
#plt.savefig("cosmo25_denslice.png")
