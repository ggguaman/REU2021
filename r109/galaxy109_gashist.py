#galaxy 109 gas histogram code
import pynbody
import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cosmo25p.768sg1bwK1BHe75.008192')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.faceon(s)

plt.hist(np.log10(s.g['temp']),color='green',bins='fd')

#customizing hist
plt.xlabel("Log(temp)")
plt.ylabel("Number of particles")
plt.title('Gas temp')

#plt.show()
plt.savefig("galaxy109_gashist.png")
