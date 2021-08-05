#gas tempurature plot
import pynbody
import numpy as np
from matplotlib import colors
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cosmo25p.768sg1bwK1BHe75.008192')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.sideon(s)

#creating slice to show gas temp
sph.image(s.g,qty="temp",width=10,denoise=True,approximate_fast=False,log=True)

plt.show()
#plt.savefig("cosmo25_tempslice.png")