#making pictures pynbody tutorial: tempurature slice with velocity plot
import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cptmarvel.5.std')
s.physical_units()

#centering halo
pynbody.analysis.angmom.sideon(s)

#creating temp slice with velocity plot
sph.image(s.g,qty="vr",width=50,denoise=True,approximate_fast=False)

#plotting BH position from findingBH.py
plt.plot(0.83406139,-0.32506914, 'ro')

#plt.show()
plt.savefig("tempslice_velocity.png")
