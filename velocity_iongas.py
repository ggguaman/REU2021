#velocity plot of ionised gas
import pynbody
import pynbody.plot.sph	as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cptmarvel.5.std')
s.physical_units()

#centering halo
pynbody.analysis.angmom.sideon(s)

sph.image(s.g,qty="vr",width=50,denoise=True,approximate_fast=False)

plt.show()
