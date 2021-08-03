import pynbody
import numpy as np
from matplotlib import colors
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cptmarvel.5.std')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.sideon(s)

#creating slice to show gas temp
#sph.image(s.g,qty="temp",width=10,denoise=True,approximate_fast=False)

#plt.show()
#plt.savefig("tempslice.png")

plt.hist(np.log10(s.g['temp']),color='green',bins='fd')

#customizing hist
plt.xlabel("Log(temp)")
plt.ylabel("Number of particles")
plt.title('Gas temp')

#plt.show()
plt.savefig("gashist.png")
