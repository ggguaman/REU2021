#velocity plot of ionised gas
import pynbody
import pynbody.plot.sph	as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cptmarvel.5.std')
s.physical_units()

#centering halo
pynbody.analysis.angmom.sideon(s)

#filter to only use ionised gas
GasFilter = pynbody.filt.HighPass('temp','4.2')

#creating image to show velocity of ionised gas
sph.image(s.g,GasFilter,qty="vr",width=10,denoise=True,approximate_fast=False,log=False)

plt.show()
