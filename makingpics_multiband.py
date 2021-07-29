#pynbody tutorial: multiband image
import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cptmarvel.5.std')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.sideon(s)

#creating image using default bands(i,v,u)
pynbody.plot.stars.render(s,width='10 kpc')

#sph.image(s.s,width=20,denoise=True,approximate_fast=False)
#plt.show()
plt.savefig("multiband.png")
