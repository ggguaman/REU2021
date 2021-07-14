#making pictures: density slice
import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt

#loading snapshot
s = pynbody.load('/mnt/data0/jillian/gguaman/cptmarvel.5.std')

#setting to physical units
s.physical_units()

#centering halo and aligning disk
pynbody.analysis.angmom.faceon(s)

#creating gas density slice
sph.image(s.g,qty="rho",units="g cm^-3",width=100)

plt.show()
