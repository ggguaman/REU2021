import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cptmarvel.5.std')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.sideon(s)

#creating slice to show gas temp
sph.image(s.g,qty="temp",width=50,denoise=True,approximate_fast=False)

plt.show()
